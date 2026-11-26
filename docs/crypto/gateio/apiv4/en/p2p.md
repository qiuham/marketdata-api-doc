---
exchange: gateio
source_url: https://www.gate.com/docs/developers/apiv4/en/p2p
api_type: REST
updated_at: 2026-11-26 18:58:20.509212
---

# P2p

P2P trading

##  Get account information🔒 Authenticated

POST`/p2p/merchant/account/get_user_info`

POST `/p2p/merchant/account/get_user_info`

_Get account information_

To query the spot account balance, use the Spot API [`GET /spot/accounts`](/docs/developers/apiv4/en/spot/#list-spot-trading-accounts).

### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pMerchantUserInfoResponse  
  
### Response Schema

Status Code **200**

P2pMerchantUserInfoResponse

Type | Constraints  
---|---  
P2pMerchantUserInfoResponse |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | number | Optional |  |   
method | string | Optional |  |   
code | integer | Optional |  |   
message | string | Optional |  |   
data | object | Optional |  |   
version | string | Optional |  |   
  
**data**

P2pMerchantUserInfo

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
is_self | boolean | Optional |  | Whether self  
user_timest | string | Optional |  | User registration time (formatted string)  
counterparties_num | integer | Optional |  | Number of counterparties  
email_verified | string | Optional |  | Whether email is verified. `1`: yes; `0`: no.  
verified | string | Optional |  | Whether KYC is completed. `1`: yes; `0`: no.  
has_phone | string | Optional |  | Whether a phone number is bound. `1`: yes; `0`: no.  
user_name | string | Optional |  | Username  
user_note | string | Optional |  | User note information  
complete_transactions | string | Optional |  | Total completed orders  
paid_transactions | string | Optional |  | Number of completed buy orders  
accepted_transactions | string | Optional |  | Number of completed sell orders  
transactions_used_time | string | Optional |  | Average time to confirm receipt  
cancelled_used_time_month | string | Optional |  | Cancellation time in last 30 days  
complete_transactions_month | string | Optional |  | Number of completed orders in last 30 days  
complete_rate_month | number | Optional |  | Completion rate in last 30 days  
orders_buy_rate_month | number | Optional |  | Buy order ratio in last 30 days  
is_black | integer | Optional |  | Whether the user is blocked. `1`: yes; `0`: no.  
is_follow | integer | Optional |  | Whether you follow this user. `1`: yes; `0`: no.  
have_traded | integer | Optional |  | Whether you have traded with this user before. `1`: yes; `0`: no.  
biz_uid | string | Optional |  | Encrypted UID  
blue_vip | integer | Optional |  | Blue V Crown Shield  
work_status | integer | Optional |  | Merchant work status  
registration_days | integer | Optional |  | Registration days  
first_trade_days | integer | Optional |  | Days since first trade  
need_replenish | integer | Optional |  | Whether additional margin is required. `1`: yes; `0`: no.  
merchant_info | object | Optional |  | Markets where user can place orders  
online_status | integer | Optional |  | Merchant online status: `1` online; `0` offline.  
work_hours | object|null | Optional | nullable: true | Merchant online status details  
transactions_month | number | Optional |  | 30-day transaction volume  
transactions_all | number | Optional |  | Total transaction volume  
trade_versatile | boolean | Optional |  | Single user or composite user  
  
**data / merchant_info**

P2pMerchantMarketInfo

Markets where user can place orders

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
type | string | Optional |  |   
market | string | Optional |  |   
  
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
    
    url = '/p2p/merchant/account/get_user_info'
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
    url="/p2p/merchant/account/get_user_info"
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
      "timestamp": 1767151138.989862,
      "method": "--",
      "code": 0,
      "message": "success",
      "data": {
        "is_self": true,
        "user_timest": "2025/11/19",
        "counterparties_num": 12,
        "email_verified": "1",
        "verified": "1",
        "has_phone": "1",
        "user_name": "merchant_demo",
        "user_note": "Preferred counterparty",
        "complete_transactions": "128",
        "paid_transactions": "68",
        "accepted_transactions": "60",
        "transactions_used_time": "300",
        "cancelled_used_time_month": "2",
        "complete_transactions_month": "32",
        "complete_rate_month": 96,
        "orders_buy_rate_month": 53,
        "is_black": 0,
        "is_follow": 0,
        "have_traded": 1,
        "biz_uid": "biz_uid_demo_9f3a7c",
        "blue_vip": 0,
        "work_status": 1,
        "registration_days": 42,
        "first_trade_days": 30,
        "need_replenish": 0,
        "merchant_info": {
          "type": "0",
          "market": "USD"
        },
        "online_status": 1,
        "work_hours": null,
        "transactions_month": 6400.5,
        "transactions_all": 28600.75,
        "trade_versatile": false
      },
      "version": "1.0.0"
    }
    

##  Get counterparty information🔒 Authenticated

POST`/p2p/merchant/account/get_counterparty_user_info`

POST `/p2p/merchant/account/get_counterparty_user_info`

_Get counterparty information_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | GetCounterpartyUserInfoRequest | Required | none  
biz_uid | body | string | Required | Counterparty crypto UID from order list or detail field `its_uid`.  
  
####  Request Body Schema

Get counterparty user info request

Request Body SchemaType | Constraints  
---|---  
GetCounterpartyUserInfoRequest | required: ["biz_uid"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
biz_uid | string | Required |  | Counterparty crypto UID from order list or detail field `its_uid`.  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pCounterpartyUserInfoResponse  
  
### Response Schema

Status Code **200**

P2pCounterpartyUserInfoResponse

Type | Constraints  
---|---  
P2pCounterpartyUserInfoResponse |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | number | Optional |  |   
method | string | Optional |  |   
code | integer | Optional |  |   
message | string | Optional |  |   
data | object | Optional |  |   
version | string | Optional |  |   
  
**data**

P2pCounterpartyUserInfo

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
user_timest | string | Optional |  | User registration time (formatted string)  
email_verified | string | Optional |  | Whether email is verified. `1`: yes; `0`: no.  
verified | string | Optional |  | Whether KYC is completed. `1`: yes; `0`: no.  
has_phone | string | Optional |  | Whether a phone number is bound. `1`: yes; `0`: no.  
user_name | string | Optional |  | Username  
user_note | string | Optional |  | User note information  
complete_transactions | string | Optional |  | Total completed orders  
paid_transactions | string | Optional |  | Number of completed buy orders  
accepted_transactions | string | Optional |  | Number of completed sell orders  
transactions_used_time | string | Optional |  | Average time to confirm receipt  
cancelled_used_time_month | string | Optional |  | Cancellation time in last 30 days  
complete_transactions_month | string | Optional |  | Number of completed orders in last 30 days  
complete_rate_month | number | Optional |  | Completion rate in last 30 days  
is_follow | integer | Optional |  | Whether you follow this user. `1`: yes; `0`: no.  
have_traded | integer | Optional |  | Whether you have traded with this user before. `1`: yes; `0`: no.  
biz_uid | string | Optional |  | Encrypted UID  
registration_days | integer | Optional |  | Registration days  
first_trade_days | integer | Optional |  | Days since first trade  
trade_versatile | boolean | Optional |  | Single user or composite user  
  
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
    
    url = '/p2p/merchant/account/get_counterparty_user_info'
    query_param = ''
    body='{"biz_uid":"biz_uid_demo_9f3a7c"}'
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
    url="/p2p/merchant/account/get_counterparty_user_info"
    query_param=""
    body_param='{"biz_uid":"biz_uid_demo_9f3a7c"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "biz_uid": "biz_uid_demo_9f3a7c"
    }
    

> Example responses

> 200 Response
    
    
    {
      "timestamp": 1767152416.755602,
      "method": "--",
      "code": 0,
      "message": "success",
      "data": {
        "user_timest": "2025/11/19",
        "email_verified": "1",
        "verified": "1",
        "has_phone": "1",
        "user_name": "counterparty_demo",
        "user_note": "",
        "complete_transactions": "86",
        "paid_transactions": "44",
        "accepted_transactions": "42",
        "transactions_used_time": "420",
        "cancelled_used_time_month": "1",
        "complete_transactions_month": "18",
        "complete_rate_month": 95,
        "is_follow": 0,
        "have_traded": 0,
        "biz_uid": "biz_uid_demo_b84d21",
        "registration_days": 180,
        "first_trade_days": 90,
        "trade_versatile": false
      },
      "version": "1.0.0"
    }
    

##  Get payment method list🔒 Authenticated

POST`/p2p/merchant/account/get_myself_payment`

POST `/p2p/merchant/account/get_myself_payment`

_Get payment method list_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | GetMyselfPaymentRequest | Optional | none  
fiat | body | string | Optional | Fiat currency; omit to return all available payment methods.  
  
####  Request Body Schema

Get payment method list request

Request Body SchemaType | Constraints  
---|---  
GetMyselfPaymentRequest |   
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
fiat | string | Optional |  | Fiat currency; omit to return all available payment methods.  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pPaymentMethodsResponse  
  
### Response Schema

Status Code **200**

P2pPaymentMethodsResponse

Type | Constraints  
---|---  
P2pPaymentMethodsResponse |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | number | Optional |  |   
method | string | Optional |  |   
code | integer | Optional |  |   
message | string | Optional |  |   
data | array | Optional |  |   
version | string | Optional |  |   
  
**data**

Type | Constraints  
---|---  
array |   
  
**data / items**

P2pPaymentMethodGroup

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
pay_type | string | Optional |  | Payment method type  
pay_name | string | Optional |  | Payment method name  
ids | array | Optional |  | User's currently bound payment method (primary key ID)  
list | array | Optional |  |   
  
**data / items / ids**

User's currently bound payment method (primary key ID)

Type | Constraints  
---|---  
array |   
  
**data / items / ids / items**

Type | Constraints  
---|---  
integer |   
  
**data / items / list**

Type | Constraints  
---|---  
array |   
  
**data / items / list / items**

P2pPaymentMethodAccount

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
uid | integer | Optional |  | useruID  
bankid | string | Optional |  | User's currently bound payment method (primary key ID)  
nickname | integer | Optional |  | Cardholder UID  
bankname | string | Optional |  | Bank name  
bankbranch | string | Optional |  | Bank branch name  
bankcity | string | Optional |  | Bank city  
bankprov | string | Optional |  | Bank province  
bankaddr | string | Optional |  | Bank card number or masked card number.  
bankdesc | string | Optional |  | Bank note  
hold_uid | integer | Optional |  | Cardholder UID  
hold_username | string | Optional |  | Cardholder name  
real_name | string | Optional |  | User verified display name.  
id | string | Optional |  | User's currently bound payment method (primary key ID)  
account_des | string | Optional |  | Payment method description  
pay_type | string | Optional |  | Payment method type  
file | string | Optional |  | Payment method file link  
file_key | string | Optional |  | Payment method file key  
account | string | Optional |  | Payment account or masked payment account.  
memo | string | Optional |  | Payment method note  
code | string | Optional |  | Payment method code  
memo_ext | string | Optional |  | Payment method additional note  
trade_tips | string | Optional |  | Payment method transaction information  
  
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
    
    url = '/p2p/merchant/account/get_myself_payment'
    query_param = ''
    body='{"fiat":"USD"}'
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
    url="/p2p/merchant/account/get_myself_payment"
    query_param=""
    body_param='{"fiat":"USD"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "fiat": "USD"
    }
    

> Example responses

> 200 Response
    
    
    {
      "timestamp": 1767152532.08744,
      "method": "--",
      "code": 0,
      "message": "success",
      "data": [
        {
          "pay_type": "bank",
          "pay_name": "Bank Transfer",
          "ids": [
            10001
          ],
          "list": [
            {
              "uid": 1000001,
              "bankid": "10001",
              "nickname": 1000001,
              "bankname": "Demo Bank",
              "bankbranch": "Main Branch",
              "bankcity": "New York",
              "bankprov": "NY",
              "bankaddr": "****1234",
              "bankdesc": "Corporate settlement account",
              "hold_uid": 1000001,
              "hold_username": "merchant_demo",
              "real_name": "Merchant Demo"
            }
          ]
        },
        {
          "pay_type": "swift",
          "pay_name": "SWIFT International Remittance",
          "ids": [
            10002
          ],
          "list": [
            {
              "id": "10002",
              "account_des": "Business USD account",
              "pay_type": "swift",
              "file": "",
              "file_key": "",
              "account": "****5678",
              "memo": "Use order txid as reference",
              "code": "",
              "memo_ext": "",
              "trade_tips": "Please pay from an account under your real name",
              "real_name": "Merchant Demo"
            }
          ]
        }
      ],
      "version": "1.0.0"
    }
    

##  Set merchant working status and custom working hours🔒 Authenticated

POST`/p2p/merchant/account/set_merchant_work_hours`

POST `/p2p/merchant/account/set_merchant_work_hours`

_Set merchant working status and custom working hours_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | SetMerchantWorkHoursRequest | Required | none  
work_status | body | integer | Required | Working status. 0: resting, 1: working, 2: using custom working hours  
cycle_type | body | string | Optional | Custom working cycle; required when work_status is 2  
day_of_week | body | string | Optional | Weekly working days, comma-separated values 1-7 for Monday to Sunday; required when work_status is 2 and cycle_type is Weekly  
time_zone | body | string | Optional | UTC timezone offset, ranging from -12 to +14; required when work_status is 2  
start_time | body | string | Optional | Custom working start time in HH:mm format; required when work_status is 2 and must not be later than end_time  
end_time | body | string | Optional | Custom working end time in HH:mm format; required when work_status is 2 and must not be earlier than start_time  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
work_status | 0  
work_status | 1  
work_status | 2  
cycle_type | Weekly  
cycle_type | Daily  
  
####  Request Body Schema

Request to set merchant working status or custom working hours

Request Body SchemaType | Constraints  
---|---  
SetMerchantWorkHoursRequest | required: ["work_status"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
work_status | integer | Required | enum: [0,1,2] | Working status. 0: resting, 1: working, 2: using custom working hours  
cycle_type | string | Optional | enum: ["Weekly","Daily"] | Custom working cycle; required when work_status is 2  
day_of_week | string | Optional |  | Weekly working days, comma-separated values 1-7 for Monday to Sunday; required when work_status is 2 and cycle_type is Weekly  
time_zone | string | Optional |  | UTC timezone offset, ranging from -12 to +14; required when work_status is 2  
start_time | string | Optional |  | Custom working start time in HH:mm format; required when work_status is 2 and must not be later than end_time  
end_time | string | Optional |  | Custom working end time in HH:mm format; required when work_status is 2 and must not be earlier than start_time  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pMerchantWorkHoursResponse  
  
### Response Schema

Status Code **200**

P2pMerchantWorkHoursResponse

Type | Constraints  
---|---  
P2pMerchantWorkHoursResponse |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | number | Optional |  | Response timestamp.  
method | string | Optional |  | Placeholder for request method.  
code | integer | Optional |  | Response code, 0 means success  
message | string | Optional |  | Response message  
data | object | Optional |  |   
version | string | Optional |  | API version.  
  
**data**

P2pMerchantWorkHours

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
work_status | integer | Optional | enum: [0,1,2,3] | Merchant's current working status. 0: normal resting, 1: normal working, 2: custom resting, 3: custom working  
  
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
    
    url = '/p2p/merchant/account/set_merchant_work_hours'
    query_param = ''
    body='{"work_status":2,"cycle_type":"Weekly","day_of_week":"1,2,3,4,5","time_zone":"+8","start_time":"09:00","end_time":"18:00"}'
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
    url="/p2p/merchant/account/set_merchant_work_hours"
    query_param=""
    body_param='{"work_status":2,"cycle_type":"Weekly","day_of_week":"1,2,3,4,5","time_zone":"+8","start_time":"09:00","end_time":"18:00"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "work_status": 2,
      "cycle_type": "Weekly",
      "day_of_week": "1,2,3,4,5",
      "time_zone": "+8",
      "start_time": "09:00",
      "end_time": "18:00"
    }
    

> Example responses

> 200 Response
    
    
    {
      "timestamp": 1767152800.123456,
      "method": "--",
      "code": 0,
      "message": "success",
      "data": {
        "work_status": 3
      },
      "version": "1.0.0"
    }
    

##  Get pending orders🔒 Authenticated

POST`/p2p/merchant/transaction/get_pending_transaction_list`

POST `/p2p/merchant/transaction/get_pending_transaction_list`

_Get pending orders_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | GetPendingTransactionListRequest | Required | none  
crypto_currency | body | string | Required | Cryptocurrency symbol.  
fiat_currency | body | string | Required | Fiat currency  
order_tab | body | string | Optional | Order tab: `pending` in progress (`OPEN`, `PAID`, `LOCKED`, `TEMP`); `dispute` in dispute; default `pending`.  
select_type | body | string | Optional | Order side filter: `buy` buy orders; `sell` sell orders; empty: all.  
status | body | string | Optional | Order status filter. `open` unpaid (`OPEN`); `paid` paid (`PAID`); `locked` locked (`LOCKED`);  
`dispute` in dispute; empty or omitted uses the default range for `order_tab`.  
txid | body | integer | Optional | Order ID  
start_time | body | integer | Optional | Start timestamp, default is 00:00 89 days ago  
end_time | body | integer | Optional | End timestamp, default is 23:59:59 today  
  
####  Detailed descriptions

** status**: Order status filter. `open` unpaid (`OPEN`); `paid` paid (`PAID`); `locked` locked (`LOCKED`);  
`dispute` in dispute; empty or omitted uses the default range for `order_tab`.

####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
order_tab | pending  
order_tab | dispute  
  
####  Request Body Schema

Get pending transaction list request

Request Body SchemaType | Constraints  
---|---  
GetPendingTransactionListRequest | required: ["crypto_currency","fiat_currency"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
crypto_currency | string | Required |  | Cryptocurrency symbol.  
fiat_currency | string | Required |  | Fiat currency  
order_tab | string | Optional | enum: ["pending","dispute"] | Order tab: `pending` in progress (`OPEN`, `PAID`, `LOCKED`, `TEMP`); `dispute` in dispute; default `pending`.  
select_type | string | Optional |  | Order side filter: `buy` buy orders; `sell` sell orders; empty: all.  
status | string | Optional |  | Order status filter. `open` unpaid (`OPEN`); `paid` paid (`PAID`); `locked` locked (`LOCKED`);  
`dispute` in dispute; empty or omitted uses the default range for `order_tab`.  
txid | integer | Optional |  | Order ID  
start_time | integer | Optional |  | Start timestamp, default is 00:00 89 days ago  
end_time | integer | Optional |  | End timestamp, default is 23:59:59 today  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pTransactionListResponse  
  
### Response Schema

Status Code **200**

P2pTransactionListResponse

Type | Constraints  
---|---  
P2pTransactionListResponse |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | number | Optional |  |   
method | string | Optional |  |   
code | integer | Optional |  |   
message | string | Optional |  |   
data | object | Optional |  |   
version | string | Optional |  |   
  
**data**

P2pTransactionListResult

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
list | array | Optional |  |   
trans_time | array | Optional |  | Countdown time  
count | integer | Optional |  | Number of orders  
exported_num | integer | Optional |  | Export count  
  
**data / list**

Type | Constraints  
---|---  
array |   
  
**data / list / items**

P2pTransactionListItem

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
type_buy | integer | Optional |  | Order side from current user's view. `1`: buy; `0`: sell.  
timest | string | Optional |  | Creation time of order  
timest_expire | string | Optional |  | Order expiration time  
timestamp | integer | Optional |  | Order creation timestamp  
rate | string | Optional |  | Order price in fiat currency.  
amount | string | Optional |  | Order size in cryptocurrency.  
total | string | Optional |  | Total fiat amount of the order.  
txid | integer | Optional |  | Order ID  
status | string | Optional |  | Display status: `unpay` awaiting payment; `paid` buyer paid; `unconfirmed` awaiting seller confirmation; `locked` locked; `finished` completed; `cancel` canceled; `expired` expired; `bclosed` arbitration filled; `sclosed` arbitration canceled.  
its_realname | string | Optional |  | Counterparty real name or verified display name.  
its_uid | string | Optional |  | Counterparty crypto UID.  
its_nick | string | Optional |  | Counterparty nickname  
seller_realname | string | Optional |  | Seller real name or verified display name.  
buyer_realname | string | Optional |  | Buyer real name or verified display name.  
cancelable | integer | Optional |  | Whether the order can be canceled. `1`: yes; `0`: no.  
currency_type | string | Optional |  | Cryptocurrency symbol.  
want_type | string | Optional |  | Fiat currency  
hide_payment | integer | Optional |  | Whether payment methods are hidden. `1`: hidden; `0`: visible.  
sel_paytype | string | Optional |  | Selected payment type for this order, e.g. `bank`, `alipay`, `wechat`, `paypal`, `swift`, `wu`.  
pay_others | array | Optional |  | Other payment method details; may appear on historical orders.  
cd_time | integer | Optional |  | Countdown seconds for the current order.  
order_type | integer | Optional |  | Order type: `1` standard; `2` partner; `3` flash swap; `4` Web3.  
order_tag | array | Optional |  | Order tags  
convert_info | object | Optional |  | Flash swap order information  
  
**data / list / items / pay_others**

Other payment method details; may appear on historical orders.

Type | Constraints  
---|---  
array |   
  
**data / list / items / pay_others / items**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
pay_type | string | Optional |  | Payment method type  
pay_name | string | Optional |  | Payment method name  
  
**data / list / items / order_tag**

Order tags

Type | Constraints  
---|---  
array |   
  
**data / list / items / order_tag / items**

Type | Constraints  
---|---  
string |   
  
**data / list / items / convert_info**

P2pTransactionConvertInfo

Flash swap order information

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
convert_type | string | Optional |  | Flash swap target currency  
convert_status | string | Optional |  | Flash swap order status  
pre_rate | string | Optional |  | Expected price when placing order  
rate | string | Optional |  | Execution price  
pre_fiat_rate | string | Optional |  | Expected fiat price when placing order  
fiat_rate | string | Optional |  | Fiat price at execution  
amount | string | Optional |  | Size  
convert_amount | string | Optional |  | Swap Amount  
slippage | string | Optional |  | Slippage calculation: slippage = (expected price when placing order - real-time price during auto swap) / expected price when placing order  
status | string | Optional |  | Flash swap order display status  
  
**data / trans_time**

Countdown time

Type | Constraints  
---|---  
array |   
  
**data / trans_time / items**

P2pTransactionTimeMarker

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
od_time | integer | Optional |  |   
  
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
    
    url = '/p2p/merchant/transaction/get_pending_transaction_list'
    query_param = ''
    body='{"crypto_currency":"USDT","fiat_currency":"USD","order_tab":"pending","select_type":"sell","status":"open","txid":40000001,"start_time":1764547200,"end_time":1767139199}'
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
    url="/p2p/merchant/transaction/get_pending_transaction_list"
    query_param=""
    body_param='{"crypto_currency":"USDT","fiat_currency":"USD","order_tab":"pending","select_type":"sell","status":"open","txid":40000001,"start_time":1764547200,"end_time":1767139199}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "crypto_currency": "USDT",
      "fiat_currency": "USD",
      "order_tab": "pending",
      "select_type": "sell",
      "status": "open",
      "txid": 40000001,
      "start_time": 1764547200,
      "end_time": 1767139199
    }
    

> Example responses

> 200 Response
    
    
    {
      "timestamp": 1767153378.888855,
      "method": "--",
      "code": 0,
      "message": "success",
      "data": {
        "list": [
          {
            "type_buy": 1,
            "timest": "2025-12-15 08:27:09",
            "timest_expire": "2025-12-15 10:27:09",
            "timestamp": 1765787229,
            "rate": "1.100",
            "amount": "8.00",
            "total": "8.800",
            "txid": 40000001,
            "status": "paid",
            "its_realname": "Counterparty Demo",
            "its_uid": "biz_uid_demo_b84d21",
            "its_nick": "counterparty_demo",
            "seller_realname": "Merchant Demo",
            "buyer_realname": "Counterparty Demo",
            "cancelable": 1,
            "currency_type": "USDT",
            "want_type": "USD",
            "hide_payment": 0,
            "sel_paytype": "bank",
            "cd_time": 600,
            "order_type": 1,
            "order_tag": [
              "fast"
            ],
            "convert_info": {}
          }
        ],
        "trans_time": [
          {
            "od_time": 600
          }
        ],
        "count": 1,
        "exported_num": 0
      },
      "version": "1.0.0"
    }
    

##  Get all/historical orders🔒 Authenticated

POST`/p2p/merchant/transaction/get_completed_transaction_list`

POST `/p2p/merchant/transaction/get_completed_transaction_list`

_Get all/historical orders_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | GetCompletedTransactionListRequest | Required | none  
crypto_currency | body | string | Required | Cryptocurrency symbol.  
fiat_currency | body | string | Required | Fiat currency  
select_type | body | string | Optional | Order side filter: `buy` buy orders; `sell` sell orders; empty: all.  
status | body | string | Optional | Order status filter. `closed`: filled (`ACCEPT`, `BCLOSED`); `cancel`: canceled (`CANCEL`, `BECANCEL`, `SCLOSED`, `SCANCEL`);  
`locked`: locked (`LOCKED`); `open`: unpaid (`OPEN`); `paid`: paid (`PAID`);  
`completed`: finished or canceled (`CANCEL`, `BECANCEL`, `SCLOSED`, `SCANCEL`, `ACCEPT`, `BCLOSED`);  
Empty or omitted uses the endpoint default range.  
txid | body | integer | Optional | Order ID  
start_time | body | integer | Optional | Start timestamp, default is 00:00 89 days ago  
end_time | body | integer | Optional | End timestamp, default is 23:59:59 today  
query_dispute | body | integer | Optional | Whether to flag dispute status in the response. `1`: yes; `0`: no.  
page | body | integer | Optional | Page number starting at 1; values below 1 are treated as 1.  
per_page | body | integer | Optional | Orders per page; default 10, max 200.  
  
####  Detailed descriptions

** status**: Order status filter. `closed`: filled (`ACCEPT`, `BCLOSED`); `cancel`: canceled (`CANCEL`, `BECANCEL`, `SCLOSED`, `SCANCEL`);  
`locked`: locked (`LOCKED`); `open`: unpaid (`OPEN`); `paid`: paid (`PAID`);  
`completed`: finished or canceled (`CANCEL`, `BECANCEL`, `SCLOSED`, `SCANCEL`, `ACCEPT`, `BCLOSED`);  
Empty or omitted uses the endpoint default range.

####  Request Body Schema

Get completed/historical transaction list request

Request Body SchemaType | Constraints  
---|---  
GetCompletedTransactionListRequest | required: ["crypto_currency","fiat_currency"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
crypto_currency | string | Required |  | Cryptocurrency symbol.  
fiat_currency | string | Required |  | Fiat currency  
select_type | string | Optional |  | Order side filter: `buy` buy orders; `sell` sell orders; empty: all.  
status | string | Optional |  | Order status filter. `closed`: filled (`ACCEPT`, `BCLOSED`); `cancel`: canceled (`CANCEL`, `BECANCEL`, `SCLOSED`, `SCANCEL`);  
`locked`: locked (`LOCKED`); `open`: unpaid (`OPEN`); `paid`: paid (`PAID`);  
`completed`: finished or canceled (`CANCEL`, `BECANCEL`, `SCLOSED`, `SCANCEL`, `ACCEPT`, `BCLOSED`);  
Empty or omitted uses the endpoint default range.  
txid | integer | Optional |  | Order ID  
start_time | integer | Optional |  | Start timestamp, default is 00:00 89 days ago  
end_time | integer | Optional |  | End timestamp, default is 23:59:59 today  
query_dispute | integer | Optional |  | Whether to flag dispute status in the response. `1`: yes; `0`: no.  
page | integer | Optional |  | Page number starting at 1; values below 1 are treated as 1.  
per_page | integer | Optional |  | Orders per page; default 10, max 200.  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pTransactionListResponse  
  
### Response Schema

Status Code **200**

P2pTransactionListResponse

Type | Constraints  
---|---  
P2pTransactionListResponse |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | number | Optional |  |   
method | string | Optional |  |   
code | integer | Optional |  |   
message | string | Optional |  |   
data | object | Optional |  |   
version | string | Optional |  |   
  
**data**

P2pTransactionListResult

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
list | array | Optional |  |   
trans_time | array | Optional |  | Countdown time  
count | integer | Optional |  | Number of orders  
exported_num | integer | Optional |  | Export count  
  
**data / list**

Type | Constraints  
---|---  
array |   
  
**data / list / items**

P2pTransactionListItem

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
type_buy | integer | Optional |  | Order side from current user's view. `1`: buy; `0`: sell.  
timest | string | Optional |  | Creation time of order  
timest_expire | string | Optional |  | Order expiration time  
timestamp | integer | Optional |  | Order creation timestamp  
rate | string | Optional |  | Order price in fiat currency.  
amount | string | Optional |  | Order size in cryptocurrency.  
total | string | Optional |  | Total fiat amount of the order.  
txid | integer | Optional |  | Order ID  
status | string | Optional |  | Display status: `unpay` awaiting payment; `paid` buyer paid; `unconfirmed` awaiting seller confirmation; `locked` locked; `finished` completed; `cancel` canceled; `expired` expired; `bclosed` arbitration filled; `sclosed` arbitration canceled.  
its_realname | string | Optional |  | Counterparty real name or verified display name.  
its_uid | string | Optional |  | Counterparty crypto UID.  
its_nick | string | Optional |  | Counterparty nickname  
seller_realname | string | Optional |  | Seller real name or verified display name.  
buyer_realname | string | Optional |  | Buyer real name or verified display name.  
cancelable | integer | Optional |  | Whether the order can be canceled. `1`: yes; `0`: no.  
currency_type | string | Optional |  | Cryptocurrency symbol.  
want_type | string | Optional |  | Fiat currency  
hide_payment | integer | Optional |  | Whether payment methods are hidden. `1`: hidden; `0`: visible.  
sel_paytype | string | Optional |  | Selected payment type for this order, e.g. `bank`, `alipay`, `wechat`, `paypal`, `swift`, `wu`.  
pay_others | array | Optional |  | Other payment method details; may appear on historical orders.  
cd_time | integer | Optional |  | Countdown seconds for the current order.  
order_type | integer | Optional |  | Order type: `1` standard; `2` partner; `3` flash swap; `4` Web3.  
order_tag | array | Optional |  | Order tags  
convert_info | object | Optional |  | Flash swap order information  
  
**data / list / items / pay_others**

Other payment method details; may appear on historical orders.

Type | Constraints  
---|---  
array |   
  
**data / list / items / pay_others / items**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
pay_type | string | Optional |  | Payment method type  
pay_name | string | Optional |  | Payment method name  
  
**data / list / items / order_tag**

Order tags

Type | Constraints  
---|---  
array |   
  
**data / list / items / order_tag / items**

Type | Constraints  
---|---  
string |   
  
**data / list / items / convert_info**

P2pTransactionConvertInfo

Flash swap order information

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
convert_type | string | Optional |  | Flash swap target currency  
convert_status | string | Optional |  | Flash swap order status  
pre_rate | string | Optional |  | Expected price when placing order  
rate | string | Optional |  | Execution price  
pre_fiat_rate | string | Optional |  | Expected fiat price when placing order  
fiat_rate | string | Optional |  | Fiat price at execution  
amount | string | Optional |  | Size  
convert_amount | string | Optional |  | Swap Amount  
slippage | string | Optional |  | Slippage calculation: slippage = (expected price when placing order - real-time price during auto swap) / expected price when placing order  
status | string | Optional |  | Flash swap order display status  
  
**data / trans_time**

Countdown time

Type | Constraints  
---|---  
array |   
  
**data / trans_time / items**

P2pTransactionTimeMarker

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
od_time | integer | Optional |  |   
  
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
    
    url = '/p2p/merchant/transaction/get_completed_transaction_list'
    query_param = ''
    body='{"crypto_currency":"USDT","fiat_currency":"USD","select_type":"buy","status":"closed","txid":40000001,"start_time":1764547200,"end_time":1767139199,"query_dispute":0,"page":1,"per_page":20}'
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
    url="/p2p/merchant/transaction/get_completed_transaction_list"
    query_param=""
    body_param='{"crypto_currency":"USDT","fiat_currency":"USD","select_type":"buy","status":"closed","txid":40000001,"start_time":1764547200,"end_time":1767139199,"query_dispute":0,"page":1,"per_page":20}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "crypto_currency": "USDT",
      "fiat_currency": "USD",
      "select_type": "buy",
      "status": "closed",
      "txid": 40000001,
      "start_time": 1764547200,
      "end_time": 1767139199,
      "query_dispute": 0,
      "page": 1,
      "per_page": 20
    }
    

> Example responses

> 200 Response
    
    
    {
      "timestamp": 1767153378.888855,
      "method": "--",
      "code": 0,
      "message": "success",
      "data": {
        "list": [
          {
            "type_buy": 1,
            "timest": "2025-12-15 08:27:09",
            "timest_expire": "2025-12-15 10:27:09",
            "timestamp": 1765787229,
            "rate": "1.100",
            "amount": "8.00",
            "total": "8.800",
            "txid": 40000001,
            "status": "finished",
            "its_realname": "Counterparty Demo",
            "its_uid": "biz_uid_demo_b84d21",
            "its_nick": "counterparty_demo",
            "seller_realname": "Merchant Demo",
            "buyer_realname": "Counterparty Demo",
            "cancelable": 0,
            "currency_type": "USDT",
            "want_type": "USD",
            "hide_payment": 0,
            "sel_paytype": "bank",
            "pay_others": [
              {
                "pay_type": "swift",
                "pay_name": "SWIFT International Remittance"
              }
            ],
            "cd_time": 0,
            "order_type": 1,
            "order_tag": [],
            "convert_info": {}
          }
        ],
        "trans_time": [
          {
            "od_time": 0
          }
        ],
        "count": 1,
        "exported_num": 0
      },
      "version": "1.0.0"
    }
    

##  Query order details🔒 Authenticated

POST`/p2p/merchant/transaction/get_transaction_details`

POST `/p2p/merchant/transaction/get_transaction_details`

_Query order details_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | GetTransactionDetailsRequest | Required | none  
txid | body | integer | Required | Order ID  
channel | body | string | Optional | Channel tag: omit or empty for normal P2P; use `web3` for Web3 orders.  
  
####  Request Body Schema

Get transaction details request

Request Body SchemaType | Constraints  
---|---  
GetTransactionDetailsRequest | required: ["txid"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
txid | integer | Required |  | Order ID  
channel | string | Optional |  | Channel tag: omit or empty for normal P2P; use `web3` for Web3 orders.  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pTransactionDetailResponse  
  
### Response Schema

Status Code **200**

P2pTransactionDetailResponse

Type | Constraints  
---|---  
P2pTransactionDetailResponse |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | number | Optional |  |   
method | string | Optional |  |   
code | integer | Optional |  |   
message | string | Optional |  |   
data | object | Optional |  |   
version | string | Optional |  |   
  
**data**

P2pTransactionDetail

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
is_sell | integer | Optional |  | Whether the current user is the seller. `1`: yes; `0`: no.  
txid | integer | Optional |  | Order ID (txid).  
orderid | integer | Optional |  | ID of the posted order (orderid).  
timest | integer | Optional |  | Order creation timestamp  
last_pay_time | integer | Optional |  | Payment deadline  
remain_pay_time | integer | Optional |  | Seconds left to pay; `<= 0` means overdue.  
currency_type | string | Optional |  | Cryptocurrency symbol.  
want_type | string | Optional |  | Fiat currency  
symbol | string | Optional |  | Fiat currency symbol  
rate | string | Optional |  | Order price in `want_type` units.  
amount | string | Optional |  | Order size in cryptocurrency.  
total | string | Optional |  | Total fiat amount of the order.  
status | string | Optional |  | Display status: `unpay` unpaid; `hide_payment` unpaid with payment info hidden; `paid` buyer paid; `unconfirmed` awaiting seller confirmation; `locked` locked; `finished` done; `cancel` canceled; `expired` expired; `bclosed` arbitration filled; `sclosed` arbitration canceled.  
reason_id | string | Optional |  | Cancel reason ID; empty string means none. Examples: `1` no longer want to buy; `2` cannot reach seller; `3` will not pay; `4` seller did not provide a real account; `6` price/amount mismatch; `9` other; `10` seller cannot release and refund issued; `11` terms not met; `12` seller payout account risk-controlled.  
reason_desc | string | Optional |  | Cancel reason description.  
cancel_time | string | Optional |  | Cancellation time  
in_appeal | integer | Optional |  | Whether a dispute is active. `1`: yes; `0`: no.  
dispute_time | integer | Optional |  | Earliest timestamp when a dispute may be opened.  
cancelable | integer | Optional |  | Whether cancellation is allowed. `1`: yes; `0`: no.  
hide_payment | integer | Optional |  | Whether payment methods are hidden. `1`: hidden; `0`: visible.  
trade_tips | string | Optional |  | Trading terms  
show_bank | string | Optional |  | Whether to show bank transfer details. `1`: show; `0`: hide.  
bankname | string | Optional |  | Bank name  
bankbranch | string | Optional |  | Bank branch name  
bankid | string | Optional |  | Bank account or masked account.  
bank_holder_realname | string | Optional |  | Bank cardholder name  
show_ali | string | Optional |  | Whether to show Alipay details. `1`: show; `0`: hide.  
aliname | string | Optional |  | Alipay account name  
is_alicode | integer | Optional |  | Whether an Alipay QR exists. `1`: yes; `0`: no.  
show_wechat | string | Optional |  | Whether to show WeChat details. `1`: show; `0`: hide.  
wename | string | Optional |  | WeChat account name  
show_others | string | Optional |  | Whether to show other payment methods. `1`: show; `0`: hide.  
pay_others | array | Optional |  | Other payment methods  
sel_paytype | string | Optional |  | Selected payment type for this order, e.g. `bank`, `alipay`, `wechat`, `paypal`, `swift`, `wu`.  
its_uid | string | Optional |  | Counterparty crypto UID.  
its_nickname | string | Optional |  | Counterparty nickname  
its_realname | string | Optional |  | Counterparty real name or verified display name.  
have_traded | integer | Optional |  | Whether you traded with the counterparty before. `1`: yes; `0`: no.  
appeal_allow_cancel | integer | Optional |  | Whether the dispute can be withdrawn. `1`: allowed; `0`: not allowed.  
appeal_verdict_has_open | string | Optional |  | Dispute outcome or in-dispute notice text.  
im_unread | integer | Optional |  | Unread chat message count.  
payment_voucher_url | array | Optional |  | Payment voucher  
timest_paid | integer | Optional |  | Timestamp when the buyer confirmed payment.  
own_realname | string | Optional |  | Current user's real name or verified display name.  
order_type | integer | Optional |  | Order type: `1` standard; `2` partner; `3` flash swap; `4` Web3.  
is_show_receive | integer | Optional |  | Whether to show confirm-receipt during dispute. `1`: show; `0`: hide.  
show_seller_contact_info | boolean | Optional |  | Whether to display seller contact information  
supported_pay_types | array | Optional |  | Supported payment method types for the order, e.g. `bank`, `alipay`, `wechat`, `paypal`, `swift`, `wu`.  
  
**data / pay_others**

Other payment methods

Type | Constraints  
---|---  
array |   
  
**data / pay_others / items**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Optional |  | Payment method record ID.  
account_des | string | Optional |  | Payment method description  
pay_type | string | Optional |  | Payment method type  
account | string | Optional |  | Payment account or masked account.  
memo | string | Optional |  | Payment note or memo.  
trade_tips | string | Optional |  | Payment instructions or tips.  
pay_name | string | Optional |  | Display name of the payment method.  
  
**data / payment_voucher_url**

Payment voucher

Type | Constraints  
---|---  
array |   
  
**data / payment_voucher_url / items**

Type | Constraints  
---|---  
string |   
  
**data / supported_pay_types**

Supported payment method types for the order, e.g. `bank`, `alipay`, `wechat`, `paypal`, `swift`, `wu`.

Type | Constraints  
---|---  
array |   
  
**data / supported_pay_types / items**

Type | Constraints  
---|---  
string |   
  
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
    
    url = '/p2p/merchant/transaction/get_transaction_details'
    query_param = ''
    body='{"txid":40000001,"channel":""}'
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
    url="/p2p/merchant/transaction/get_transaction_details"
    query_param=""
    body_param='{"txid":40000001,"channel":""}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "txid": 40000001,
      "channel": ""
    }
    

> Example responses

> 200 Response
    
    
    {
      "timestamp": 1767859489.457123,
      "method": "--",
      "code": 0,
      "message": "success",
      "data": {
        "is_sell": 1,
        "txid": 40000001,
        "orderid": 2124000001,
        "timest": 1767530241,
        "last_pay_time": 1767531441,
        "remain_pay_time": 600,
        "currency_type": "USDT",
        "want_type": "USD",
        "symbol": "$",
        "rate": "1.230",
        "amount": "3",
        "total": "3.690",
        "status": "paid",
        "reason_id": "",
        "reason_desc": "",
        "cancel_time": "",
        "in_appeal": 0,
        "dispute_time": 0,
        "cancelable": 1,
        "hide_payment": 0,
        "trade_tips": "Please pay from an account under your real name",
        "show_bank": "1",
        "bankname": "Demo Bank",
        "bankbranch": "Main Branch",
        "bankid": "****1234",
        "bank_holder_realname": "Merchant Demo",
        "show_ali": "0",
        "aliname": "",
        "is_alicode": 0,
        "show_wechat": "0",
        "wename": "",
        "show_others": "0",
        "pay_others": [],
        "sel_paytype": "bank",
        "its_uid": "biz_uid_demo_b84d21",
        "its_nickname": "counterparty_demo",
        "its_realname": "Counterparty Demo",
        "have_traded": 1,
        "appeal_allow_cancel": 0,
        "appeal_verdict_has_open": "",
        "im_unread": 0,
        "payment_voucher_url": [],
        "timest_paid": 1767530257,
        "own_realname": "Merchant Demo",
        "order_type": 1,
        "is_show_receive": 0,
        "show_seller_contact_info": false,
        "supported_pay_types": [
          "bank",
          "swift"
        ]
      },
      "version": "1.0.0"
    }
    

##  Confirm payment🔒 Authenticated

POST`/p2p/merchant/transaction/confirm-payment`

POST `/p2p/merchant/transaction/confirm-payment`

_Confirm payment_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | ConfirmPayment | Required | none  
txid | body | string | Required | Order ID  
payment_method | body | string | Optional | Payment type used for this payment; optional but must be among order-supported types. Use `supported_pay_types` on the order or `pay_type` list, e.g. `bank`, `alipay`, `wechat`, `paypal`, `swift`, `wu`.  
  
####  Request Body Schema

Confirm payment request

Request Body SchemaType | Constraints  
---|---  
ConfirmPayment | required: ["txid"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
txid | string | Required |  | Order ID  
payment_method | string | Optional |  | Payment type used for this payment; optional but must be among order-supported types. Use `supported_pay_types` on the order or `pay_type` list, e.g. `bank`, `alipay`, `wechat`, `paypal`, `swift`, `wu`.  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pTransactionActionResponse  
  
### Response Schema

Status Code **200**

P2pTransactionActionResponse

Type | Constraints  
---|---  
P2pTransactionActionResponse |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | number | Optional |  | Response timestamp.  
method | string | Optional |  | Placeholder for request method.  
code | integer | Optional |  | Response code, 0 means success  
message | string | Optional |  | Response message  
data | object | Optional |  | Empty object on success.  
version | string | Optional |  | API version.  
  
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
    
    url = '/p2p/merchant/transaction/confirm-payment'
    query_param = ''
    body='{"txid":"40000001","payment_method":"bank"}'
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
    url="/p2p/merchant/transaction/confirm-payment"
    query_param=""
    body_param='{"txid":"40000001","payment_method":"bank"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "txid": "40000001",
      "payment_method": "bank"
    }
    

> Example responses

> 200 Response
    
    
    {
      "timestamp": 1767009886.638032,
      "method": "--",
      "code": 0,
      "message": "success",
      "data": {},
      "version": "1.0.0"
    }
    

##  Confirm receipt🔒 Authenticated

POST`/p2p/merchant/transaction/confirm-receipt`

POST `/p2p/merchant/transaction/confirm-receipt`

_Confirm receipt_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | ConfirmReceipt | Required | none  
txid | body | string | Required | Order ID  
  
####  Request Body Schema

Confirm receipt request

Request Body SchemaType | Constraints  
---|---  
ConfirmReceipt | required: ["txid"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
txid | string | Required |  | Order ID  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pTransactionActionResponse  
  
### Response Schema

Status Code **200**

P2pTransactionActionResponse

Type | Constraints  
---|---  
P2pTransactionActionResponse |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | number | Optional |  | Response timestamp.  
method | string | Optional |  | Placeholder for request method.  
code | integer | Optional |  | Response code, 0 means success  
message | string | Optional |  | Response message  
data | object | Optional |  | Empty object on success.  
version | string | Optional |  | API version.  
  
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
    
    url = '/p2p/merchant/transaction/confirm-receipt'
    query_param = ''
    body='{"txid":"40000001"}'
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
    url="/p2p/merchant/transaction/confirm-receipt"
    query_param=""
    body_param='{"txid":"40000001"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "txid": "40000001"
    }
    

> Example responses

> 200 Response
    
    
    {
      "timestamp": 1767009886.638032,
      "method": "--",
      "code": 0,
      "message": "success",
      "data": {},
      "version": "1.0.0"
    }
    

##  Cancel order🔒 Authenticated

POST`/p2p/merchant/transaction/cancel`

POST `/p2p/merchant/transaction/cancel`

_Cancel order_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | CancelOrder | Required | none  
txid | body | string | Required | Order ID  
reason_id | body | string | Optional | Cancel reason ID. `1` no longer want to buy; `2` cannot reach seller; `3` will not pay; `4` seller account not real; `5` payout account issue; `6` price mismatch; `7` mutually agreed cancel; `8` poor communication; `9` other; `10` seller cannot release with refund; `11` terms not met; `12` seller payout risk-controlled.  
reason_memo | body | string | Optional | Extra cancel notes when `reason_id` is `9` or explanation is required.  
  
####  Request Body Schema

Cancel order request

Request Body SchemaType | Constraints  
---|---  
CancelOrder | required: ["txid"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
txid | string | Required |  | Order ID  
reason_id | string | Optional |  | Cancel reason ID. `1` no longer want to buy; `2` cannot reach seller; `3` will not pay; `4` seller account not real; `5` payout account issue; `6` price mismatch; `7` mutually agreed cancel; `8` poor communication; `9` other; `10` seller cannot release with refund; `11` terms not met; `12` seller payout risk-controlled.  
reason_memo | string | Optional |  | Extra cancel notes when `reason_id` is `9` or explanation is required.  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pTransactionActionResponse  
  
### Response Schema

Status Code **200**

P2pTransactionActionResponse

Type | Constraints  
---|---  
P2pTransactionActionResponse |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | number | Optional |  | Response timestamp.  
method | string | Optional |  | Placeholder for request method.  
code | integer | Optional |  | Response code, 0 means success  
message | string | Optional |  | Response message  
data | object | Optional |  | Empty object on success.  
version | string | Optional |  | API version.  
  
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
    
    url = '/p2p/merchant/transaction/cancel'
    query_param = ''
    body='{"txid":"40000001","reason_id":"1","reason_memo":"Canceled after agreement with the counterparty"}'
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
    url="/p2p/merchant/transaction/cancel"
    query_param=""
    body_param='{"txid":"40000001","reason_id":"1","reason_memo":"Canceled after agreement with the counterparty"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "txid": "40000001",
      "reason_id": "1",
      "reason_memo": "Canceled after agreement with the counterparty"
    }
    

> Example responses

> 200 Response
    
    
    {
      "timestamp": 1767009886.638032,
      "method": "--",
      "code": 0,
      "message": "success",
      "data": {},
      "version": "1.0.0"
    }
    

##  Publish ad order🔒 Authenticated

POST`/p2p/merchant/books/place_biz_push_order`

POST `/p2p/merchant/books/place_biz_push_order`

_Publish ad order_

When publishing or editing an advertisement, trade_tips and auto_reply go through off-platform traffic diversion risk control; when hit, the advertisement is not saved, and code 70305102 with data.risk_event is returned.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | PlaceBizPushOrder | Required | none  
currencyType | body | string | Required | Cryptocurrency symbol.  
exchangeType | body | string | Required | Fiat currency  
type | body | string | Required | Ad operation type. `0`: publish sell ad; `1`: publish buy ad; `2`: edit sell ad; `3`: edit buy ad.  
unitPrice | body | string | Required | Per-unit price in fixed-price mode.  
number | body | string | Required | Ad amount priced in `currencyType`.  
payType | body | string | Required | Payment types enabled for the ad, comma-separated; values can be obtained from `pay_type` in the payment method list, e.g. `bank`, `alipay`, `wechat`, `paypal`, `swift`, `wu`. `pay_type_json` uses the types in this field as keys to specify the corresponding payment accounts.  
pay_type_json | body | string | Optional | JSON string of specific payment accounts corresponding to `payType`. Each key is a payment type listed in `payType`, and each value is the current user's payment method ID for that type. For example, when `payType` is `bank,swift`, this field can be {"bank":"10001","swift":"10002"}.  
rateFixed | body | string | Optional | Price type: `0` floating; `1` fixed.  
oid | body | string | Optional | Pass ad ID when editing; omit or empty when publishing a new ad.  
minAmount | body | string | Optional | Minimum quantity per order, denominated by currencyType; required when limitBasis is not passed or is 0  
maxAmount | body | string | Optional | Maximum quantity per order, denominated by currencyType; required when limitBasis is not passed or is 0  
limitBasis | body | integer | Optional | Trading limit unit. 0: by crypto quantity, 1: by fiat amount; defaults to 0 when not passed for a new ad. The limit unit of an existing ad cannot be changed when editing; a fiat-limit ad must keep passing 1 when edited  
fiatMinAmount | body | string | Optional | Minimum amount per order, denominated by exchangeType; required when limitBasis is 1  
fiatMaxAmount | body | string | Optional | Maximum amount per order, denominated by exchangeType; required when limitBasis is 1, and must not exceed the total fiat value of the ad quantity converted at the price  
tierLimit | body | string | Optional | Minimum counterparty VIP level; `0` means no requirement.  
verifiedLimit | body | string | Optional | Minimum counterparty verification level; `0` means no limit.  
regTimeLimit | body | string | Optional | Minimum counterparty account age in days; `0` means no limit.  
advertisersLimit | body | string | Optional | Whether trading with the advertiser is restricted. `0`: no; `1`: yes.  
polymarket_limit | body | integer | Optional | Whether to restrict trading with Polymarket users. 0: no restriction, 1: restricted  
expire_min | body | string | Optional | Payment timeout in minutes.  
trade_tips | body | string | Optional | Advertisement trade terms displayed to ordering users; goes through off-platform traffic diversion risk control on submission, and when hit, the advertisement is not saved and code 70305102 is returned  
auto_reply | body | string | Optional | Auto reply content after order creation; goes through off-platform traffic diversion risk control on submission, and when hit, the advertisement is not saved and code 70305102 is returned  
min_completed_limit | body | string | Optional | Minimum completed orders for counterparty; `-1` unlimited.  
max_completed_limit | body | string | Optional | Maximum completed orders for counterparty; `-1` unlimited.  
completed_rate_limit | body | string | Optional | Counterparty minimum 30-day completion rate; `-1` means no limit.  
user_country_limit | body | string | Optional | KYC nationality restriction; `-1` means no restriction.  
user_order_limit | body | string | Optional | Maximum concurrent orders allowed for the counterparty. `-1`: unlimited.  
rateReferenceId | body | string | Optional | Floating price reference. `1`: platform reference; `2`: Gate reference; `3`: spot reference.  
rateOffset | body | string | Optional | Absolute floating offset ratio, e.g. `0.5` means 0.5%.  
float_trend | body | string | Optional | Floating direction: `0` markup; `1` markdown.  
team_payment_uid | body | string | Optional | Team payee UID; optional for non-team merchants.  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
type | 0  
type | 1  
type | 2  
type | 3  
limitBasis | 0  
limitBasis | 1  
polymarket_limit | 0  
polymarket_limit | 1  
  
####  Request Body Schema

Place ad order request

Request Body SchemaType | Constraints  
---|---  
PlaceBizPushOrder | required: ["currencyType","exchangeType","type","unitPrice","number","payType"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
currencyType | string | Required |  | Cryptocurrency symbol.  
exchangeType | string | Required |  | Fiat currency  
type | string | Required | enum: ["0","1","2","3"] | Ad operation type. `0`: publish sell ad; `1`: publish buy ad; `2`: edit sell ad; `3`: edit buy ad.  
unitPrice | string | Required |  | Per-unit price in fixed-price mode.  
number | string | Required |  | Ad amount priced in `currencyType`.  
payType | string | Required |  | Payment types enabled for the ad, comma-separated; values can be obtained from `pay_type` in the payment method list, e.g. `bank`, `alipay`, `wechat`, `paypal`, `swift`, `wu`. `pay_type_json` uses the types in this field as keys to specify the corresponding payment accounts.  
pay_type_json | string | Optional |  | JSON string of specific payment accounts corresponding to `payType`. Each key is a payment type listed in `payType`, and each value is the current user's payment method ID for that type. For example, when `payType` is `bank,swift`, this field can be {"bank":"10001","swift":"10002"}.  
rateFixed | string | Optional |  | Price type: `0` floating; `1` fixed.  
oid | string | Optional |  | Pass ad ID when editing; omit or empty when publishing a new ad.  
minAmount | string | Optional |  | Minimum quantity per order, denominated by currencyType; required when limitBasis is not passed or is 0  
maxAmount | string | Optional |  | Maximum quantity per order, denominated by currencyType; required when limitBasis is not passed or is 0  
limitBasis | integer | Optional | enum: [0,1] | Trading limit unit. 0: by crypto quantity, 1: by fiat amount; defaults to 0 when not passed for a new ad. The limit unit of an existing ad cannot be changed when editing; a fiat-limit ad must keep passing 1 when edited  
fiatMinAmount | string | Optional |  | Minimum amount per order, denominated by exchangeType; required when limitBasis is 1  
fiatMaxAmount | string | Optional |  | Maximum amount per order, denominated by exchangeType; required when limitBasis is 1, and must not exceed the total fiat value of the ad quantity converted at the price  
tierLimit | string | Optional |  | Minimum counterparty VIP level; `0` means no requirement.  
verifiedLimit | string | Optional |  | Minimum counterparty verification level; `0` means no limit.  
regTimeLimit | string | Optional |  | Minimum counterparty account age in days; `0` means no limit.  
advertisersLimit | string | Optional |  | Whether trading with the advertiser is restricted. `0`: no; `1`: yes.  
polymarket_limit | integer | Optional | enum: [0,1] | Whether to restrict trading with Polymarket users. 0: no restriction, 1: restricted  
expire_min | string | Optional |  | Payment timeout in minutes.  
trade_tips | string | Optional |  | Advertisement trade terms displayed to ordering users; goes through off-platform traffic diversion risk control on submission, and when hit, the advertisement is not saved and code 70305102 is returned  
auto_reply | string | Optional |  | Auto reply content after order creation; goes through off-platform traffic diversion risk control on submission, and when hit, the advertisement is not saved and code 70305102 is returned  
min_completed_limit | string | Optional |  | Minimum completed orders for counterparty; `-1` unlimited.  
max_completed_limit | string | Optional |  | Maximum completed orders for counterparty; `-1` unlimited.  
completed_rate_limit | string | Optional |  | Counterparty minimum 30-day completion rate; `-1` means no limit.  
user_country_limit | string | Optional |  | KYC nationality restriction; `-1` means no restriction.  
user_order_limit | string | Optional |  | Maximum concurrent orders allowed for the counterparty. `-1`: unlimited.  
rateReferenceId | string | Optional |  | Floating price reference. `1`: platform reference; `2`: Gate reference; `3`: spot reference.  
rateOffset | string | Optional |  | Absolute floating offset ratio, e.g. `0.5` means 0.5%.  
float_trend | string | Optional |  | Floating direction: `0` markup; `1` markdown.  
team_payment_uid | string | Optional |  | Team payee UID; optional for non-team merchants.  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pMerchantBooksPlaceBizPushOrderResponse  
  
### Response Schema

Status Code **200**

P2pMerchantBooksPlaceBizPushOrderResponse

Type | Constraints  
---|---  
P2pMerchantBooksPlaceBizPushOrderResponse |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | number | Optional |  | Response timestamp.  
method | string | Optional |  | Placeholder for request method.  
code | integer | Optional |  | Response code. 0 means success; 70305102 means the advertisement trade terms or auto reply hit off-platform traffic diversion risk control  
message | string | Optional |  | Response message  
data | object | Optional |  | Empty object when the advertisement is published or edited successfully; returns risk details when the advertisement content hits risk control  
version | string | Optional |  | API version.  
  
**data**

Empty object when the advertisement is published or edited successfully; returns risk details when the advertisement content hits risk control

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
risk_code | integer | Optional |  | Risk control sub-code; 0 for advertisement content traffic diversion risk control  
risk_event | object | Optional |  | Risk control prompt event for advertisement content  
  
**data / risk_event**

Risk control prompt event for advertisement content

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
type | string | Optional | enum: ["modal"] | Prompt display type  
title | string | Optional |  | Risk control prompt title  
msg | string | Optional |  | Risk control prompt message generated based on the field that hit risk control  
action | array | Optional |  | Available actions; advertisement content risk control only returns the close action  
content_risk_type | string | Optional | enum: ["trade_tips","auto_reply","trade_tips_auto_reply"] | Advertisement content field that hit risk control  
trade_tips | string | Optional |  | Prompt message returned when the trade terms hit risk control  
auto_reply | string | Optional |  | Prompt message returned when the auto reply hits risk control  
  
**data / risk_event / action**

Available actions; advertisement content risk control only returns the close action

Type | Constraints  
---|---  
array |   
  
**data / risk_event / action / items**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
action_type | string | Optional | enum: ["close"] | Action type  
title | string | Optional |  | Action button text  
mainly | integer | Optional | enum: [0] | Whether it is the primary action. 0: no  
action_data | object | Optional |  | Additional data of the action; empty object for the close action  
  
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
    
    url = '/p2p/merchant/books/place_biz_push_order'
    query_param = ''
    body='{"currencyType":"USDT","exchangeType":"USD","type":"0","unitPrice":"1.1","number":"100","payType":"bank,swift","pay_type_json":"{\"bank\":\"10001\",\"swift\":\"10002\"}","rateFixed":"1","oid":"2124000001","minAmount":"10","maxAmount":"500","limitBasis":1,"fiatMinAmount":"100","fiatMaxAmount":"1000","tierLimit":"0","verifiedLimit":"0","regTimeLimit":"0","advertisersLimit":"0","polymarket_limit":0,"expire_min":"20","trade_tips":"Please pay from an account under your own name","auto_reply":"Please tap Paid after completing the transfer","min_completed_limit":"-1","max_completed_limit":"-1","completed_rate_limit":"-1","user_country_limit":"-1","user_order_limit":"-1","rateReferenceId":"3","rateOffset":"0.5","float_trend":"0","team_payment_uid":"1000001"}'
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
    url="/p2p/merchant/books/place_biz_push_order"
    query_param=""
    body_param='{"currencyType":"USDT","exchangeType":"USD","type":"0","unitPrice":"1.1","number":"100","payType":"bank,swift","pay_type_json":"{\"bank\":\"10001\",\"swift\":\"10002\"}","rateFixed":"1","oid":"2124000001","minAmount":"10","maxAmount":"500","limitBasis":1,"fiatMinAmount":"100","fiatMaxAmount":"1000","tierLimit":"0","verifiedLimit":"0","regTimeLimit":"0","advertisersLimit":"0","polymarket_limit":0,"expire_min":"20","trade_tips":"Please pay from an account under your own name","auto_reply":"Please tap Paid after completing the transfer","min_completed_limit":"-1","max_completed_limit":"-1","completed_rate_limit":"-1","user_country_limit":"-1","user_order_limit":"-1","rateReferenceId":"3","rateOffset":"0.5","float_trend":"0","team_payment_uid":"1000001"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "currencyType": "USDT",
      "exchangeType": "USD",
      "type": "0",
      "unitPrice": "1.1",
      "number": "100",
      "payType": "bank,swift",
      "pay_type_json": "{\"bank\":\"10001\",\"swift\":\"10002\"}",
      "rateFixed": "1",
      "oid": "2124000001",
      "minAmount": "10",
      "maxAmount": "500",
      "limitBasis": 1,
      "fiatMinAmount": "100",
      "fiatMaxAmount": "1000",
      "tierLimit": "0",
      "verifiedLimit": "0",
      "regTimeLimit": "0",
      "advertisersLimit": "0",
      "polymarket_limit": 0,
      "expire_min": "20",
      "trade_tips": "Please pay from an account under your own name",
      "auto_reply": "Please tap Paid after completing the transfer",
      "min_completed_limit": "-1",
      "max_completed_limit": "-1",
      "completed_rate_limit": "-1",
      "user_country_limit": "-1",
      "user_order_limit": "-1",
      "rateReferenceId": "3",
      "rateOffset": "0.5",
      "float_trend": "0",
      "team_payment_uid": "1000001"
    }
    

> Example responses

> 200 Response
    
    
    {
      "timestamp": 1767009886.638032,
      "method": "--",
      "code": 0,
      "message": "success",
      "data": {},
      "version": "1.0.0"
    }
    

##  Update ad status🔒 Authenticated

POST`/p2p/merchant/books/ads_update_status`

POST `/p2p/merchant/books/ads_update_status`

_Update ad status_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | AdsUpdateStatus | Required | none  
adv_no | body | integer | Required | Advertisement ID.  
adv_status | body | integer | Required | Ad status. `1`: listed; `3`: delisted; `4`: closed.  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
adv_status | 1  
adv_status | 3  
adv_status | 4  
  
####  Request Body Schema

Ad status update request

Request Body SchemaType | Constraints  
---|---  
AdsUpdateStatus | required: ["adv_no","adv_status"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
adv_no | integer | Required |  | Advertisement ID.  
adv_status | integer | Required | enum: [1,3,4] | Ad status. `1`: listed; `3`: delisted; `4`: closed.  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pAdsUpdateStatusResponse  
  
### Response Schema

Status Code **200**

P2pAdsUpdateStatusResponse

Type | Constraints  
---|---  
P2pAdsUpdateStatusResponse |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | number | Optional |  |   
method | string | Optional |  |   
code | integer | Optional |  |   
message | string | Optional |  |   
data | object | Optional |  |   
version | string | Optional |  |   
  
**data**

P2pAdsUpdateStatusResult

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
status | integer | Optional |  | Ad status after update: `1` listed; `3` delisted; `4` closed.  
  
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
    
    url = '/p2p/merchant/books/ads_update_status'
    query_param = ''
    body='{"adv_no":2124000001,"adv_status":3}'
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
    url="/p2p/merchant/books/ads_update_status"
    query_param=""
    body_param='{"adv_no":2124000001,"adv_status":3}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "adv_no": 2124000001,
      "adv_status": 3
    }
    

> Example responses

> 200 Response
    
    
    {
      "timestamp": 1767009886.638032,
      "method": "--",
      "code": 0,
      "message": "success",
      "data": {
        "status": 3
      },
      "version": "1.0.0"
    }
    

##  Query ad details🔒 Authenticated

POST`/p2p/merchant/books/ads_detail`

POST `/p2p/merchant/books/ads_detail`

_Query ad details_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | AdsDetailRequest | Required | none  
adv_no | body | string | Required | Advertisement ID.  
  
####  Request Body Schema

Get ad details request

Request Body SchemaType | Constraints  
---|---  
AdsDetailRequest | required: ["adv_no"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
adv_no | string | Required |  | Advertisement ID.  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pAdDetailResponse  
  
### Response Schema

Status Code **200**

P2pAdDetailResponse

Type | Constraints  
---|---  
P2pAdDetailResponse |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | number | Optional |  |   
method | string | Optional |  |   
code | integer | Optional |  |   
message | string | Optional |  |   
data | object | Optional |  |   
version | string | Optional |  |   
  
**data**

P2pAdDetail

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
rate | string | Optional |  | Advertisement price.  
type | string | Optional |  | Ad side: `buy` buy-crypto ad; `sell` sell-crypto ad.  
amount | string | Optional |  | Remaining crypto amount on the ad.  
min_amount | string | Optional |  | Minimum quantity per order, denominated by currency_type  
max_amount | string | Optional |  | Maximum quantity per order, denominated by currency_type  
fiat_min_amount | string | Optional |  | Minimum trade amount in `want_type`.  
fiat_max_amount | string | Optional |  | Maximum trade amount priced in `want_type`.  
limit_basis | integer | Optional | enum: [0,1] | Trading limit unit. 0: crypto quantity, 1: fiat amount  
limit_basis_text | string | Optional | enum: ["crypto","fiat"] | Trading limit unit label. crypto: crypto quantity, fiat: fiat amount  
total | string | Optional |  | Fiat amount  
pay_ali | integer | Optional |  | Whether Alipay is supported. `1`: yes; `0`: no.  
pay_bank | integer | Optional |  | Whether bank transfer is supported. `1`: yes; `0`: no.  
pay_paypal | integer | Optional |  | Whether PayPal is supported. `1`: yes; `0`: no.  
pay_wechat | integer | Optional |  | Whether WeChat Pay is supported. `1`: yes; `0`: no.  
pay_type_num | string | Optional |  | Payment method ID list  
pay_type_json | string | Optional |  | JSON map of payment type -> payment method ID.  
locked_amount | string | Optional |  | Locked amount  
orderid | integer | Optional |  | Order ID  
timestamp | integer | Optional |  | Created time  
currency_type | string | Optional |  | Cryptocurrency symbol.  
want_type | string | Optional |  | Fiat type  
hide_rate | string | Optional |  | Hidden price  
trade_tips | string | Optional |  | Trading terms  
auto_reply | string | Optional |  | Auto reply  
rate_ref_id | integer | Optional |  | Floating reference: `1` platform; `2` Gate; `3` spot; `<= 0` means fixed price.  
rate_offset | number | Optional |  | Floating ratio (absolute value)  
status | string | Optional |  | Ad status: `OPEN` listed; `OFFLIN` delisted; `CLOSED` closed; `CANCEL` canceled.  
rate_fixed | integer | Optional |  | Price type: `0` floating; `1` fixed.  
float_trend | integer | Optional |  | Floating direction: `0` markup; `1` markdown.  
expire_min | integer | Optional |  | Timeout (minutes)  
tier_limit | integer | Optional |  | Tier limit  
reg_time_limit | integer | Optional |  | Registration time limit  
advertisers_limit | integer | Optional |  | Whether trading with the advertiser is restricted. `0`: no; `1`: yes.  
polymarket_limit | integer | Optional |  | Whether to restrict trading with Polymarket users. 0: no restriction, 1: restricted  
min_completed_limit | integer | Optional |  | Minimum limit of completed orders  
max_completed_limit | integer | Optional |  | Maximum limit of completed orders  
user_orders_limit | integer | Optional |  | Order count limit  
completed_rate_limit | number | Optional |  | 30-day completion rate limit  
limit_country_cn | string | Optional |  | Restricted nationality (Chinese)  
limit_country_en | string | Optional |  | Restricted nationality (English)  
is_hedge | integer | Optional |  | Whether auto-delegation is enabled. `1`: yes; `0`: no.  
hide_payment | integer | Optional |  | Whether payment methods are hidden. `1`: hidden; `0`: visible.  
  
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
    
    url = '/p2p/merchant/books/ads_detail'
    query_param = ''
    body='{"adv_no":"2124000001"}'
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
    url="/p2p/merchant/books/ads_detail"
    query_param=""
    body_param='{"adv_no":"2124000001"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "adv_no": "2124000001"
    }
    

> Example responses

> 200 Response
    
    
    {
      "timestamp": 1767149820.871772,
      "method": "--",
      "code": 0,
      "message": "Success",
      "data": {
        "rate": "0.908",
        "type": "sell",
        "amount": "100.00",
        "min_amount": "10",
        "max_amount": "500",
        "fiat_min_amount": "9.08",
        "fiat_max_amount": "454.00",
        "limit_basis": 0,
        "limit_basis_text": "crypto",
        "total": "90.800",
        "pay_ali": 0,
        "pay_bank": 1,
        "pay_paypal": 0,
        "pay_wechat": 0,
        "pay_type_num": "2,5",
        "pay_type_json": "{\"bank\":\"10001\",\"swift\":\"10002\"}",
        "locked_amount": "0",
        "orderid": 2124000001,
        "timestamp": 1766988136,
        "currency_type": "USDT",
        "want_type": "USD",
        "hide_rate": "0.000",
        "trade_tips": "Please pay from an account under your real name",
        "auto_reply": "Thanks for your order. I will process it soon.",
        "rate_ref_id": 3,
        "rate_offset": 0.5,
        "status": "OPEN",
        "rate_fixed": 0,
        "float_trend": 0,
        "expire_min": 20,
        "tier_limit": 0,
        "reg_time_limit": 0,
        "advertisers_limit": 0,
        "polymarket_limit": 0,
        "min_completed_limit": -1,
        "max_completed_limit": -1,
        "user_orders_limit": -1,
        "completed_rate_limit": -1,
        "limit_country_cn": "",
        "limit_country_en": "",
        "is_hedge": 0,
        "hide_payment": 0
      },
      "version": "1.0.0"
    }
    

##  Get my ad list🔒 Authenticated

POST`/p2p/merchant/books/my_ads_list`

POST `/p2p/merchant/books/my_ads_list`

_Get my ad list_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | MyAdsListRequest | Optional | none  
asset | body | string | Optional | Crypto asset; omit to skip asset filter.  
fiat_unit | body | string | Optional | Fiat currency; omit to skip fiat filter.  
trade_type | body | string | Optional | Ad side: `buy` for buy-crypto ads, `sell` for sell-crypto ads; omit for all sides.  
  
####  Request Body Schema

Get my ads list request

Request Body SchemaType | Constraints  
---|---  
MyAdsListRequest |   
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
asset | string | Optional |  | Crypto asset; omit to skip asset filter.  
fiat_unit | string | Optional |  | Fiat currency; omit to skip fiat filter.  
trade_type | string | Optional |  | Ad side: `buy` for buy-crypto ads, `sell` for sell-crypto ads; omit for all sides.  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pMyAdsListResponse  
  
### Response Schema

Status Code **200**

P2pMyAdsListResponse

Type | Constraints  
---|---  
P2pMyAdsListResponse |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | number | Optional |  |   
method | string | Optional |  |   
code | integer | Optional |  |   
message | string | Optional |  |   
data | object | Optional |  |   
version | string | Optional |  | Version number  
  
**data**

P2pMyAdsListResult

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
lists | array | Optional |  |   
  
**data / lists**

Type | Constraints  
---|---  
array |   
  
**data / lists / items**

P2pMyAd

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
type | string | Optional |  | Ad side: `buy` buy-crypto ad; `sell` sell-crypto ad.  
rate | string | Optional |  | Price  
original_rate | string | Optional |  | Original price  
amount | string | Optional |  | Remaining crypto amount on the ad.  
total | string | Optional |  | Remaining fiat amount of ad  
limit_total | string | Optional |  | Single order limit range (cryptocurrency)  
limit_fiat | string | Optional |  | Single order limit range (fiat)  
min_amount | string | Optional |  | Minimum quantity per order  
max_amount | string | Optional |  | Maximum quantity per order  
pay_type_num | string | Optional |  | Payment method ID list  
pay_type_json | string | Optional |  | JSON map of payment type -> payment method ID.  
expire_min | string | Optional |  | Ad expiration time (minutes)  
tier_limit | string | Optional |  | VIP limit  
advertisers_limit | integer | Optional |  | Whether trading with the advertiser is restricted. `0`: no; `1`: yes.  
reg_time_limit | integer | Optional |  | Registration time limit  
verified_limit | integer | Optional |  | KYC level limit  
min_completed_limit | integer | Optional |  | Minimum limit of completed orders by counterparty  
max_completed_limit | integer | Optional |  | Maximum limit of completed orders by counterparty  
user_country_limit | integer | Optional |  | KYC nationality restriction  
completed_rate_limit | number | Optional |  | 30-day completion rate limit  
user_orders_limit | integer | Optional |  | Maximum order limit for counterparty  
hide_payment | string | Optional |  | Whether payment methods are hidden. `1`: hidden; `0`: visible.  
currencyType | string | Optional |  | Cryptocurrency symbol.  
want_type | string | Optional |  | Fiat currency  
trade_tips | string | Optional |  | Trading terms  
new_hand | integer | Optional |  | Special ad type. `0` normal; `1` newcomer guide; `2` newcomer discount; `3` featured promo; `4` KOL ad; `5` coupon ad.  
id | string | Optional |  | Advertisement ID.  
status | string | Optional |  | Ad status: `OPEN` listed; `OFFLIN` delisted; `CLOSED` closed; `CANCEL` canceled.  
locked_amount | string | Optional |  | Ad frozen amount  
hide_rate | string | Optional |  | Hidden price  
is_out_time | integer | Optional |  | Whether the ad timed out. `1`: timed out; `0`: not yet.  
rate_ref_id | integer | Optional |  | Floating reference: `1` platform; `2` Gate; `3` spot; `<= 0` means fixed price.  
rate_offset | string | Optional |  | Floating ratio  
rate_fixed | integer | Optional |  | Price type: `0` floating; `1` fixed.  
float_trend | integer | Optional |  | Floating direction: `0` markup; `1` markdown.  
in_dispute | integer | Optional |  | Whether the ad had a disputed trade. `1`: yes; `0`: no.  
auto_reply | string | Optional |  | Auto reply data  
timestamp | integer | Optional |  | Ad creation time  
is_hedge | integer | Optional |  | Whether auto-delegation is enabled. `1`: yes; `0`: no.  
  
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
    
    url = '/p2p/merchant/books/my_ads_list'
    query_param = ''
    body='{"asset":"USDT","fiat_unit":"USD","trade_type":"sell"}'
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
    url="/p2p/merchant/books/my_ads_list"
    query_param=""
    body_param='{"asset":"USDT","fiat_unit":"USD","trade_type":"sell"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "asset": "USDT",
      "fiat_unit": "USD",
      "trade_type": "sell"
    }
    

> Example responses

> 200 Response
    
    
    {
      "timestamp": 1767088873.074896,
      "method": "--",
      "code": 0,
      "message": "Success",
      "data": {
        "lists": [
          {
            "type": "sell",
            "rate": "1.270",
            "original_rate": "1.270",
            "amount": "100.00",
            "total": "127.000",
            "limit_total": "10~500",
            "limit_fiat": "12.7~635",
            "min_amount": "10",
            "max_amount": "500",
            "pay_type_num": "2,4",
            "pay_type_json": "{\"bank\":\"10001\",\"wu\":\"10003\"}",
            "expire_min": "45",
            "tier_limit": "1",
            "advertisers_limit": 1,
            "reg_time_limit": 90,
            "verified_limit": 0,
            "min_completed_limit": 8,
            "max_completed_limit": 9,
            "user_country_limit": 4,
            "completed_rate_limit": 6,
            "user_orders_limit": 7,
            "hide_payment": "1",
            "currencyType": "USDT",
            "want_type": "USD",
            "trade_tips": "Please pay from an account under your real name",
            "new_hand": 0,
            "id": "2124000001",
            "status": "OFFLIN",
            "locked_amount": "0",
            "hide_rate": "0.000",
            "is_out_time": 0,
            "rate_ref_id": -1,
            "rate_offset": "0",
            "rate_fixed": 1,
            "float_trend": 0,
            "in_dispute": 0,
            "auto_reply": "Thanks for your order. I will process it soon.",
            "timestamp": 1767008930,
            "is_hedge": 0
          }
        ]
      },
      "version": "1.0.0"
    }
    

##  Get Advertisement List🔒 Authenticated

POST`/p2p/merchant/books/ads_list`

POST `/p2p/merchant/books/ads_list`

_Get Advertisement List_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | AdsListRequest | Required | none  
asset | body | string | Required | Cryptocurrency symbol.  
fiat_unit | body | string | Required | Fiat currency  
trade_type | body | string | Required | Ad side: `buy` buy-crypto ad; `sell` sell-crypto ad.  
  
####  Request Body Schema

Get market ads list request

Request Body SchemaType | Constraints  
---|---  
AdsListRequest | required: ["asset","fiat_unit","trade_type"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
asset | string | Required |  | Cryptocurrency symbol.  
fiat_unit | string | Required |  | Fiat currency  
trade_type | string | Required |  | Ad side: `buy` buy-crypto ad; `sell` sell-crypto ad.  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pAdsListResponse  
  
### Response Schema

Status Code **200**

P2pAdsListResponse

Type | Constraints  
---|---  
P2pAdsListResponse |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | number | Optional |  |   
method | string | Optional |  |   
code | integer | Optional |  |   
message | string | Optional |  |   
data | array | Optional |  |   
version | string | Optional |  |   
  
**data**

Type | Constraints  
---|---  
array |   
  
**data / items**

P2pAdsListItem

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
index | integer | Optional |  | Serial number  
asset | string | Optional |  | Cryptocurrency  
fiat_unit | string | Optional |  | Fiat currency  
adv_no | integer | Optional |  | Ad ID  
price | string | Optional |  | Price  
surplus_amount | string | Optional |  | Remaining tradable crypto quantity  
max_single_trans_amount | string | Optional |  | Maximum crypto size per trade.  
min_single_trans_amount | string | Optional |  | Minimum crypto size per trade.  
fiat_min_amount | string | Optional |  | Minimum fiat amount per order  
fiat_max_amount | string | Optional |  | Maximum fiat amount per order  
limit_basis | integer | Optional | enum: [0,1] | Trading limit unit. 0: crypto quantity, 1: fiat amount  
limit_basis_text | string | Optional | enum: ["crypto","fiat"] | Trading limit unit label. crypto: crypto quantity, fiat: fiat amount  
trade_methods | array | Optional |  | Supported payment methods list  
nick_name | string | Optional |  | Advertiser Nickname  
  
**data / items / trade_methods**

Supported payment methods list

Type | Constraints  
---|---  
array |   
  
**data / items / trade_methods / items**

P2pAdsListTradeMethod

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
icon_url_color | string | Optional |  | Payment method color icon URL  
identifier | string | Optional |  | Payment method identifier  
pay_id | string | Optional |  | Payment method ID  
pay_type | string | Optional |  | Payment method type  
trade_method_name | string | Optional |  | Payment method name  
  
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
    
    url = '/p2p/merchant/books/ads_list'
    query_param = ''
    body='{"asset":"USDT","fiat_unit":"USD","trade_type":"sell"}'
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
    url="/p2p/merchant/books/ads_list"
    query_param=""
    body_param='{"asset":"USDT","fiat_unit":"USD","trade_type":"sell"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "asset": "USDT",
      "fiat_unit": "USD",
      "trade_type": "sell"
    }
    

> Example responses

> 200 Response
    
    
    {
      "timestamp": 1769573081.981503,
      "method": "--",
      "code": 0,
      "message": "success",
      "data": [
        {
          "index": 1,
          "asset": "USDT",
          "fiat_unit": "USD",
          "adv_no": 2124000001,
          "price": "0.800",
          "surplus_amount": "4975.5",
          "max_single_trans_amount": "4975.5",
          "min_single_trans_amount": "1",
          "fiat_min_amount": "0.80",
          "fiat_max_amount": "3980.40",
          "limit_basis": 0,
          "limit_basis_text": "crypto",
          "trade_methods": [
            {
              "icon_url_color": "https://www.gate.com/images/payment/bank.png",
              "identifier": "bank",
              "pay_id": "10001",
              "pay_type": "bank",
              "trade_method_name": "Bank Transfer"
            }
          ],
          "nick_name": "merchant_demo_01"
        },
        {
          "index": 2,
          "asset": "USDT",
          "fiat_unit": "USD",
          "adv_no": 2124000002,
          "price": "0.880",
          "surplus_amount": "12379.15",
          "max_single_trans_amount": "12379.15",
          "min_single_trans_amount": "10",
          "fiat_min_amount": "8.80",
          "fiat_max_amount": "10893.65",
          "limit_basis": 1,
          "limit_basis_text": "fiat",
          "trade_methods": [
            {
              "icon_url_color": "https://www.gate.com/images/payment/swift.png",
              "identifier": "swift",
              "pay_id": "10002",
              "pay_type": "swift",
              "trade_method_name": "SWIFT"
            }
          ],
          "nick_name": "merchant_demo_02"
        },
        {
          "index": 3,
          "asset": "USDT",
          "fiat_unit": "USD",
          "adv_no": 2124000003,
          "price": "1.000",
          "surplus_amount": "2",
          "max_single_trans_amount": "2",
          "min_single_trans_amount": "1",
          "fiat_min_amount": "1.00",
          "fiat_max_amount": "2.00",
          "limit_basis": 0,
          "limit_basis_text": "crypto",
          "trade_methods": [
            {
              "icon_url_color": "https://www.gate.com/images/payment/paypal.png",
              "identifier": "paypal",
              "pay_id": "10003",
              "pay_type": "paypal",
              "trade_method_name": "PayPal"
            }
          ],
          "nick_name": "merchant_demo_03"
        }
      ],
      "version": "1.0.0"
    }
    

##  Get chat history🔒 Authenticated

POST`/p2p/merchant/chat/get_chats_list`

POST `/p2p/merchant/chat/get_chats_list`

_Get chat history_

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | GetChatsListRequest | Required | none  
txid | body | integer | Optional | Order ID; omit or `0` to return the latest order with chat for the user.  
lastreceived | body | integer | Optional | Timestamp of the last received message for backward incremental fetch; omit on first load.  
firstreceived | body | integer | Optional | Timestamp of first received message for paging backward; omit on first load.  
  
####  Request Body Schema

Get chat history request

Request Body SchemaType | Constraints  
---|---  
GetChatsListRequest |   
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
txid | integer | Optional |  | Order ID; omit or `0` to return the latest order with chat for the user.  
lastreceived | integer | Optional |  | Timestamp of the last received message for backward incremental fetch; omit on first load.  
firstreceived | integer | Optional |  | Timestamp of first received message for paging backward; omit on first load.  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pChatListResponse  
  
### Response Schema

Status Code **200**

P2pChatListResponse

Type | Constraints  
---|---  
P2pChatListResponse |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | number | Optional |  |   
method | string | Optional |  |   
code | integer | Optional |  |   
message | string | Optional |  |   
data | object | Optional |  |   
version | string | Optional |  |   
  
**data**

P2pChatListResult

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
messages | array | Optional |  | Message List  
memo | string | Optional |  | Payment tip (displayed on homepage only)  
has_history | boolean | Optional |  | Whether historical records exist  
txid | integer | Optional |  | Order ID  
SRVTM | integer | Optional |  | Timestamp of the latest message.  
order_status | string | Optional |  | Raw order status in DB; typical values: `OPEN`, `PAID`, `LOCKED`, `ACCEPT`, `BCLOSED`, `CANCEL`, `BECANCEL`, `SCLOSED`, `SCANCEL`.  
  
**data / messages**

Message List

Type | Constraints  
---|---  
array |   
  
**data / messages / items**

P2pChatMessage

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
is_sell | integer | Optional |  | Whether the current user is the seller. `1`: yes; `0`: no.  
msg_type | integer | Optional |  | Message type: `0` text; `1` file; `2` template; `3` order-share; `4` payment-share; `5` status update.  
msg | string | Optional |  | Message content; for file messages, usually URL or file key.  
username | string | Optional |  | Message sender username  
timest | integer | Optional |  | Message timestamp  
msg_obj | object | Optional |  |   
uid | string | Optional |  | Sender's crypto UID; system messages may use `System` or an empty string.  
type | integer | Optional |  | Display type: `1` file message; `2` system message.  
pic | string | Optional |  | File link  
file_key | string | Optional |  | File key  
file_type | string | Optional |  | File type: `image` for images, `video` for videos.  
risk_type | integer | Optional | enum: [1] | Risk control display type. 1: off-platform traffic diversion risk; returned when a text message hits risk control  
toast_msg | string | Optional |  | Risk control prompt message; returned only when risk_type=1  
  
**data / messages / items / msg_obj**

P2pChatMessagePayload

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
status | string | Optional |  | Order status when sending a message. Typical values: `OPEN`, `PAID`, `LOCKED`, `ACCEPT`, `BCLOSED`, `CANCEL`, `BECANCEL`, `SCLOSED`, `SCANCEL`.  
text | string | Optional |  | Message content  
payment_voucher | array | Optional |  | Payment voucher  
reason_id | integer | Optional |  | Cancel reason ID. `1` no longer want to buy; `2` cannot reach seller; `3` will not pay; `4` seller account not real; `5` payout account issue; `6` price mismatch; `7` mutually agreed cancel; `8` poor communication; `9` other; `10` seller cannot release with refund; `11` terms not met; `12` seller payout risk-controlled.  
toast_id | integer | Optional |  | Cancellation reason popup  
reason_memo | string | Optional |  | Cancel reason description.  
cancel_time | integer | Optional |  | Cancellation time  
seller_confirm | integer | Optional |  | Seller confirmation of cancel reason: `0` pending; `1` confirmed; `2` rejected.  
id | string | Optional |  | Payment method information ID  
account_des | string | Optional |  | Payment method description  
pay_type | string | Optional |  | Payment method type  
file | string | Optional |  | Payment method file link  
file_key | string | Optional |  | Payment method file key  
account | string | Optional |  | Payment account or masked payment account.  
memo | string | Optional |  | Payment method note  
code | string | Optional |  | Payment method code  
memo_ext | string | Optional |  | Payment method additional note  
trade_tips | string | Optional |  | Payment method tip  
real_name | string | Optional |  | Payment method username  
is_delete | integer | Optional |  | Whether the payment method was deleted. `1`: deleted; `0`: not deleted.  
pay_name | string | Optional |  | Payment method full name  
  
**data / messages / items / msg_obj / payment_voucher**

Payment voucher

Type | Constraints  
---|---  
array |   
  
**data / messages / items / msg_obj / payment_voucher / items**

Type | Constraints  
---|---  
string |   
  
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
    
    url = '/p2p/merchant/chat/get_chats_list'
    query_param = ''
    body='{"txid":40000001,"lastreceived":1767009884,"firstreceived":1767009000}'
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
    url="/p2p/merchant/chat/get_chats_list"
    query_param=""
    body_param='{"txid":40000001,"lastreceived":1767009884,"firstreceived":1767009000}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "txid": 40000001,
      "lastreceived": 1767009884,
      "firstreceived": 1767009000
    }
    

> Example responses

> 200 Response
    
    
    {
      "timestamp": 1767086748.178922,
      "method": "--",
      "code": 0,
      "message": "success",
      "data": {
        "messages": [
          {
            "is_sell": 1,
            "msg_type": 0,
            "msg": "Please tap Paid after completing the transfer",
            "username": "Self",
            "timest": 1767009000
          },
          {
            "is_sell": 1,
            "msg_type": 0,
            "msg": "Please contact me outside Gate",
            "username": "Self",
            "timest": 1767009001,
            "risk_type": 1,
            "toast_msg": "This message may contain security risks."
          },
          {
            "is_sell": 1,
            "msg_type": 5,
            "msg": "",
            "username": "Other",
            "msg_obj": {
              "status": "OPEN",
              "text": "Order created. Awaiting buyer's payment.",
              "payment_voucher": []
            },
            "uid": "",
            "timest": 1767009001
          },
          {
            "is_sell": 1,
            "msg_type": 5,
            "msg": "",
            "username": "Other",
            "msg_obj": {
              "status": "CANCEL",
              "text": "The buyer has canceled the order.",
              "reason_id": 1,
              "toast_id": 1,
              "reason_memo": "I don't want to buy the coins anymore.",
              "cancel_time": 1767009300,
              "seller_confirm": 0,
              "payment_voucher": []
            },
            "uid": "",
            "timest": 1767009300
          },
          {
            "uid": "System",
            "username": "System",
            "type": 2,
            "msg": "Please keep all communication within the Gate platform.",
            "timest": 1767009400
          },
          {
            "is_sell": 1,
            "msg_type": 4,
            "msg": "",
            "username": "Other",
            "uid": "biz_uid_demo_b84d21",
            "timest": 1767009500,
            "msg_obj": {
              "id": "10002",
              "account_des": "Business USD account",
              "pay_type": "swift",
              "file": "",
              "file_key": "",
              "account": "****5678",
              "memo": "Use order txid as reference",
              "code": "",
              "memo_ext": "",
              "trade_tips": "Please pay from an account under your real name",
              "real_name": "Merchant Demo",
              "is_delete": 1,
              "pay_name": "SWIFT International Remittance"
            }
          },
          {
            "is_sell": 1,
            "msg_type": 0,
            "msg": "Payment completed, please check",
            "username": "Other",
            "timest": 1767009600
          },
          {
            "is_sell": 1,
            "msg_type": 1,
            "msg": "https://example.com/p2p/chat/receipt.png",
            "username": "Other",
            "timest": 1767009700,
            "pic": "https://example.com/p2p/chat/receipt.png",
            "file_key": "c2cchat_image/c2ctrade-demo-receipt|s3-gateio-payments",
            "file_type": "image",
            "type": 1
          }
        ],
        "memo": "",
        "has_history": false,
        "txid": 40000001,
        "SRVTM": 1767009700,
        "order_status": "CANCEL"
      },
      "version": "1.0.0"
    }
    

##  Send text message🔒 Authenticated

POST`/p2p/merchant/chat/send_chat_message`

POST `/p2p/merchant/chat/send_chat_message`

_Send text message_

Text messages go through off-platform traffic diversion risk control. When hit, the API still returns code 0, and data contains risk_type=1 and toast_msg.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | SendChatMessageRequest | Required | none  
txid | body | integer | Required | Order ID  
type | body | integer | Optional | Message type: 0 for text, 1 for files. Defaults to 0 when omitted.  
message | body | string | Required | Message content. For type=0, provide text up to 500 characters. Off-platform solicitation risk checks may return risk_type=1 and toast_msg. For type=1, after a successful S3 upload, provide the file_key returned by pre_upload_chat_file.  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
type | 0  
type | 1  
  
####  Request Body Schema

Send chat message request

Request Body SchemaType | Constraints  
---|---  
SendChatMessageRequest | required: ["txid","message"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
txid | integer | Required |  | Order ID  
type | integer | Optional | enum: [0,1] | Message type: 0 for text, 1 for files. Defaults to 0 when omitted.  
message | string | Required |  | Message content. For type=0, provide text up to 500 characters. Off-platform solicitation risk checks may return risk_type=1 and toast_msg. For type=1, after a successful S3 upload, provide the file_key returned by pre_upload_chat_file.  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pSendChatMessageResponse  
  
### Response Schema

Status Code **200**

P2pSendChatMessageResponse

Type | Constraints  
---|---  
P2pSendChatMessageResponse |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | number | Optional |  |   
method | string | Optional |  |   
code | integer | Optional |  |   
message | string | Optional |  |   
data | object | Optional |  |   
version | string | Optional |  |   
  
**data**

P2pSendChatMessageResult

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
SRVTM | integer | Optional |  | Timestamp when message was successfully sent (current timestamp)  
txid | integer | Optional |  | Order ID  
conversation_id | string | Optional |  | Chat ID, formatted as both parties' UIDs concatenated in ascending order  
msg_type | integer | Optional | enum: [0] | Message content type when risk control is hit. 0: text  
risk_type | integer | Optional | enum: [1] | Risk control display type. 1: off-platform traffic diversion risk; returned only when risk control is hit  
toast_msg | string | Optional |  | Risk control prompt message; returned only when risk_type=1  
  
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
    
    url = '/p2p/merchant/chat/send_chat_message'
    query_param = ''
    body='{"txid":40000001,"type":0,"message":"Payment completed, please check"}'
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
    url="/p2p/merchant/chat/send_chat_message"
    query_param=""
    body_param='{"txid":40000001,"type":0,"message":"Payment completed, please check"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "txid": 40000001,
      "type": 0,
      "message": "Payment completed, please check"
    }
    

> Example responses

> 200 Response
    
    
    {
      "timestamp": 1767009886.638032,
      "method": "--",
      "code": 0,
      "message": "success",
      "data": {
        "SRVTM": 1767009886638,
        "txid": 40000001,
        "conversation_id": "1000001_1000002",
        "msg_type": 0,
        "risk_type": 1,
        "toast_msg": "This message may contain security risks."
      },
      "version": "1.0.0"
    }
    

##  Upload chat file🔒 Authenticated

POST`/p2p/merchant/chat/upload_chat_file`

POST `/p2p/merchant/chat/upload_chat_file`

_Upload chat file_

This endpoint is deprecated. Use Pre-upload chat file to obtain credentials for direct S3 uploads.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | UploadChatFile | Required | none  
image_content_type | body | string | Required | File MIME type: supports `image/jpeg`, `image/jpg`, `image/png`, `video/mp4`.  
base64_img | body | string | Required | Base64-encoded file content.  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
image_content_type | image/jpeg  
image_content_type | image/jpg  
image_content_type | image/png  
image_content_type | video/mp4  
  
####  Request Body Schema

Upload chat file request

Request Body SchemaType | Constraints  
---|---  
UploadChatFile | required: ["image_content_type","base64_img"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
image_content_type | string | Required | enum: ["image/jpeg","image/jpg","image/png","video/mp4"] | File MIME type: supports `image/jpeg`, `image/jpg`, `image/png`, `video/mp4`.  
base64_img | string | Required |  | Base64-encoded file content.  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pUploadChatFileResponse  
  
### Response Schema

Status Code **200**

P2pUploadChatFileResponse

Type | Constraints  
---|---  
P2pUploadChatFileResponse |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | number | Optional |  |   
method | string | Optional |  |   
code | integer | Optional |  |   
message | string | Optional |  |   
data | object | Optional |  |   
version | string | Optional |  |   
  
**data**

P2pUploadChatFileResult

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
file_key | string | Optional |  | File key  
  
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
    
    url = '/p2p/merchant/chat/upload_chat_file'
    query_param = ''
    body='{"image_content_type":"image/png","base64_img":"iVBORw0KGgoAAAANSUhEUgAAAAEAAAAB..."}'
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
    url="/p2p/merchant/chat/upload_chat_file"
    query_param=""
    body_param='{"image_content_type":"image/png","base64_img":"iVBORw0KGgoAAAANSUhEUgAAAAEAAAAB..."}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "image_content_type": "image/png",
      "base64_img": "iVBORw0KGgoAAAANSUhEUgAAAAEAAAAB..."
    }
    

> Example responses

> 200 Response
    
    
    {
      "timestamp": 1767009875.525072,
      "method": "--",
      "code": 0,
      "message": "success",
      "data": {
        "file_key": "c2cchat_image/c2ctrade-demo-receipt|s3-gateio-payments"
      },
      "version": "1.0.0"
    }
    

##  Pre-upload chat file🔒 Authenticated

POST`/p2p/merchant/chat/pre_upload_chat_file`

POST `/p2p/merchant/chat/pre_upload_chat_file`

_Pre-upload chat file_

Get credentials for a direct S3 upload of a chat file. Credentials expire after 45 minutes. The maximum file size is 100 MiB.

Upload the file using the returned url and fields, placing the file field last in the form. After S3 returns HTTP 204, call send_chat_message with type=1 and the returned file_key as message.

### Parameters

ParametersName | In | Type | Required | Description  
---|---|---|---|---  
body | body | PreUploadChatFileRequest | Required | none  
content_type | body | string | Required | File MIME type.  
  
####  Enumerated Values

Enumerated ValuesParameter | Value  
---|---  
content_type | image/jpeg  
content_type | image/jpg  
content_type | image/png  
content_type | image/webp  
content_type | video/mp4  
  
####  Request Body Schema

Request credentials for a direct chat file upload

Request Body SchemaType | Constraints  
---|---  
PreUploadChatFileRequest | required: ["content_type"]  
  
**Properties**

Request Body SchemaName | Type | Required | Constraints | Description  
---|---|---|---|---  
content_type | string | Required | enum: ["image/jpeg","image/jpg","image/png","image/webp","video/mp4"] | File MIME type.  
  
### Responses

ResponsesStatus | Meaning | Description | Schema  
---|---|---|---  
200 | [OK ](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | P2pPreUploadChatFileResponse  
  
### Response Schema

Status Code **200**

P2pPreUploadChatFileResponse

Type | Constraints  
---|---  
P2pPreUploadChatFileResponse |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | number | Optional |  |   
method | string | Optional |  |   
code | integer | Optional |  |   
message | string | Optional |  |   
data | P2pPreUploadChatFileResult | Optional |  |   
version | string | Optional |  |   
  
**data**

P2pPreUploadChatFileResult

Type | Constraints  
---|---  
P2pPreUploadChatFileResult |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
url | string | Optional |  | S3 POST upload URL. Use it before the credentials expire.  
fields | object | Optional |  | Signed S3 form fields. Submit all keys and values unchanged when uploading.  
file_key | string | Optional |  | Chat file identifier. After uploading, use it as message in send_chat_message with type=1.  
  
**data / fields**

Signed S3 form fields. Submit all keys and values unchanged when uploading.

Type | Constraints  
---|---  
object |   
  
**data / fields / additionalProperties**

Type | Constraints  
---|---  
string |   
  
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
    
    url = '/p2p/merchant/chat/pre_upload_chat_file'
    query_param = ''
    body='{"content_type":"image/png"}'
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
    url="/p2p/merchant/chat/pre_upload_chat_file"
    query_param=""
    body_param='{"content_type":"image/png"}'
    timestamp=$(date +%s)
    body_hash=$(printf "$body_param" | openssl sha512 | awk '{print $NF}')
    sign_string="$method\n$prefix$url\n$query_param\n$body_hash\n$timestamp"
    sign=$(printf "$sign_string" | openssl sha512 -hmac "$secret" | awk '{print $NF}')
    
    full_url="$host$prefix$url"
    curl -X $method $full_url -d "$body_param" -H "Content-Type: application/json" \
        -H "Timestamp: $timestamp" -H "KEY: $key" -H "SIGN: $sign"
    
    

> Body parameter
    
    
    {
      "content_type": "image/png"
    }
    

> Example responses

> 200 Response
    
    
    {
      "timestamp": 1767009875.525072,
      "method": "--",
      "code": 0,
      "message": "success",
      "data": {
        "url": "https://example-bucket.s3.ap-northeast-1.amazonaws.com/",
        "fields": {
          "key": "c2cchat_image/example-receipt.png",
          "Content-Type": "image/png",
          "X-Amz-Algorithm": "AWS4-HMAC-SHA256",
          "X-Amz-Credential": "EXAMPLE/20261117/ap-northeast-1/s3/aws4_request",
          "X-Amz-Date": "20261117T000000Z",
          "X-Amz-Security-Token": "example-session-token",
          "Policy": "example-policy",
          "X-Amz-Signature": "example-signature"
        },
        "file_key": "c2cchat_image/example-receipt.png|s3-gateio-payments"
      },
      "version": "1.0.0"
    }
    

#  Schemas

##  P2pCounterpartyUserInfoResponse

P2pCounterpartyUserInfoResponse

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | number | Optional |  |   
method | string | Optional |  |   
code | integer | Optional |  |   
message | string | Optional |  |   
data | object | Optional |  |   
version | string | Optional |  |   
  
**data**

P2pCounterpartyUserInfo

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
user_timest | string | Optional |  | User registration time (formatted string)  
email_verified | string | Optional |  | Whether email is verified. `1`: yes; `0`: no.  
verified | string | Optional |  | Whether KYC is completed. `1`: yes; `0`: no.  
has_phone | string | Optional |  | Whether a phone number is bound. `1`: yes; `0`: no.  
user_name | string | Optional |  | Username  
user_note | string | Optional |  | User note information  
complete_transactions | string | Optional |  | Total completed orders  
paid_transactions | string | Optional |  | Number of completed buy orders  
accepted_transactions | string | Optional |  | Number of completed sell orders  
transactions_used_time | string | Optional |  | Average time to confirm receipt  
cancelled_used_time_month | string | Optional |  | Cancellation time in last 30 days  
complete_transactions_month | string | Optional |  | Number of completed orders in last 30 days  
complete_rate_month | number | Optional |  | Completion rate in last 30 days  
is_follow | integer | Optional |  | Whether you follow this user. `1`: yes; `0`: no.  
have_traded | integer | Optional |  | Whether you have traded with this user before. `1`: yes; `0`: no.  
biz_uid | string | Optional |  | Encrypted UID  
registration_days | integer | Optional |  | Registration days  
first_trade_days | integer | Optional |  | Days since first trade  
trade_versatile | boolean | Optional |  | Single user or composite user  
      
    
    {
      "timestamp": 0,
      "method": "string",
      "code": 0,
      "message": "string",
      "data": {
        "user_timest": "string",
        "email_verified": "string",
        "verified": "string",
        "has_phone": "string",
        "user_name": "string",
        "user_note": "string",
        "complete_transactions": "string",
        "paid_transactions": "string",
        "accepted_transactions": "string",
        "transactions_used_time": "string",
        "cancelled_used_time_month": "string",
        "complete_transactions_month": "string",
        "complete_rate_month": 0,
        "is_follow": 0,
        "have_traded": 0,
        "biz_uid": "string",
        "registration_days": 0,
        "first_trade_days": 0,
        "trade_versatile": true
      },
      "version": "string"
    }
    
    

##  GetCompletedTransactionListRequest

Get completed/historical transaction list request

Type | Constraints  
---|---  
object | required: ["crypto_currency","fiat_currency"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
crypto_currency | string | Required |  | Cryptocurrency symbol.  
fiat_currency | string | Required |  | Fiat currency  
select_type | string | Optional |  | Order side filter: `buy` buy orders; `sell` sell orders; empty: all.  
status | string | Optional |  | Order status filter. `closed`: filled (`ACCEPT`, `BCLOSED`); `cancel`: canceled (`CANCEL`, `BECANCEL`, `SCLOSED`, `SCANCEL`);  
`locked`: locked (`LOCKED`); `open`: unpaid (`OPEN`); `paid`: paid (`PAID`);  
`completed`: finished or canceled (`CANCEL`, `BECANCEL`, `SCLOSED`, `SCANCEL`, `ACCEPT`, `BCLOSED`);  
Empty or omitted uses the endpoint default range.  
txid | integer | Optional |  | Order ID  
start_time | integer | Optional |  | Start timestamp, default is 00:00 89 days ago  
end_time | integer | Optional |  | End timestamp, default is 23:59:59 today  
query_dispute | integer | Optional |  | Whether to flag dispute status in the response. `1`: yes; `0`: no.  
page | integer | Optional |  | Page number starting at 1; values below 1 are treated as 1.  
per_page | integer | Optional |  | Orders per page; default 10, max 200.  
      
    
    {
      "crypto_currency": "USDT",
      "fiat_currency": "USD",
      "select_type": "buy",
      "status": "closed",
      "txid": 40000001,
      "start_time": 1764547200,
      "end_time": 1767139199,
      "query_dispute": 0,
      "page": 1,
      "per_page": 20
    }
    
    

##  P2pMerchantWorkHoursResponse

P2pMerchantWorkHoursResponse

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | number | Optional |  | Response timestamp.  
method | string | Optional |  | Placeholder for request method.  
code | integer | Optional |  | Response code, 0 means success  
message | string | Optional |  | Response message  
data | object | Optional |  |   
version | string | Optional |  | API version.  
  
**data**

P2pMerchantWorkHours

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
work_status | integer | Optional | enum: [0,1,2,3] | Merchant's current working status. 0: normal resting, 1: normal working, 2: custom resting, 3: custom working  
      
    
    {
      "timestamp": 0,
      "method": "string",
      "code": 0,
      "message": "string",
      "data": {
        "work_status": 0
      },
      "version": "string"
    }
    
    

##  P2pSendChatMessageResponse

P2pSendChatMessageResponse

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | number | Optional |  |   
method | string | Optional |  |   
code | integer | Optional |  |   
message | string | Optional |  |   
data | object | Optional |  |   
version | string | Optional |  |   
  
**data**

P2pSendChatMessageResult

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
SRVTM | integer | Optional |  | Timestamp when message was successfully sent (current timestamp)  
txid | integer | Optional |  | Order ID  
conversation_id | string | Optional |  | Chat ID, formatted as both parties' UIDs concatenated in ascending order  
msg_type | integer | Optional | enum: [0] | Message content type when risk control is hit. 0: text  
risk_type | integer | Optional | enum: [1] | Risk control display type. 1: off-platform traffic diversion risk; returned only when risk control is hit  
toast_msg | string | Optional |  | Risk control prompt message; returned only when risk_type=1  
      
    
    {
      "timestamp": 0,
      "method": "string",
      "code": 0,
      "message": "string",
      "data": {
        "SRVTM": 0,
        "txid": 0,
        "conversation_id": "string",
        "msg_type": 0,
        "risk_type": 1,
        "toast_msg": "string"
      },
      "version": "string"
    }
    
    

##  SendChatMessageRequest

Send chat message request

Type | Constraints  
---|---  
object | required: ["txid","message"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
txid | integer | Required |  | Order ID  
type | integer | Optional | enum: [0,1] | Message type: 0 for text, 1 for files. Defaults to 0 when omitted.  
message | string | Required |  | Message content. For type=0, provide text up to 500 characters. Off-platform solicitation risk checks may return risk_type=1 and toast_msg. For type=1, after a successful S3 upload, provide the file_key returned by pre_upload_chat_file.  
      
    
    {
      "txid": 40000001,
      "type": 0,
      "message": "Payment completed, please check"
    }
    
    

##  GetTransactionDetailsRequest

Get transaction details request

Type | Constraints  
---|---  
object | required: ["txid"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
txid | integer | Required |  | Order ID  
channel | string | Optional |  | Channel tag: omit or empty for normal P2P; use `web3` for Web3 orders.  
      
    
    {
      "txid": 40000001,
      "channel": ""
    }
    
    

##  GetChatsListRequest

Get chat history request

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
txid | integer | Optional |  | Order ID; omit or `0` to return the latest order with chat for the user.  
lastreceived | integer | Optional |  | Timestamp of the last received message for backward incremental fetch; omit on first load.  
firstreceived | integer | Optional |  | Timestamp of first received message for paging backward; omit on first load.  
      
    
    {
      "txid": 40000001,
      "lastreceived": 1767009884,
      "firstreceived": 1767009000
    }
    
    

##  PreUploadChatFileRequest

Request credentials for a direct chat file upload

Type | Constraints  
---|---  
object | required: ["content_type"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
content_type | string | Required | enum: ["image/jpeg","image/jpg","image/png","image/webp","video/mp4"] | File MIME type.  
      
    
    {
      "content_type": "image/png"
    }
    
    

##  P2pMyAdsListResponse

P2pMyAdsListResponse

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | number | Optional |  |   
method | string | Optional |  |   
code | integer | Optional |  |   
message | string | Optional |  |   
data | object | Optional |  |   
version | string | Optional |  | Version number  
  
**data**

P2pMyAdsListResult

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
lists | array | Optional |  |   
  
**data / lists**

Type | Constraints  
---|---  
array |   
  
**data / lists / items**

P2pMyAd

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
type | string | Optional |  | Ad side: `buy` buy-crypto ad; `sell` sell-crypto ad.  
rate | string | Optional |  | Price  
original_rate | string | Optional |  | Original price  
amount | string | Optional |  | Remaining crypto amount on the ad.  
total | string | Optional |  | Remaining fiat amount of ad  
limit_total | string | Optional |  | Single order limit range (cryptocurrency)  
limit_fiat | string | Optional |  | Single order limit range (fiat)  
min_amount | string | Optional |  | Minimum quantity per order  
max_amount | string | Optional |  | Maximum quantity per order  
pay_type_num | string | Optional |  | Payment method ID list  
pay_type_json | string | Optional |  | JSON map of payment type -> payment method ID.  
expire_min | string | Optional |  | Ad expiration time (minutes)  
tier_limit | string | Optional |  | VIP limit  
advertisers_limit | integer | Optional |  | Whether trading with the advertiser is restricted. `0`: no; `1`: yes.  
reg_time_limit | integer | Optional |  | Registration time limit  
verified_limit | integer | Optional |  | KYC level limit  
min_completed_limit | integer | Optional |  | Minimum limit of completed orders by counterparty  
max_completed_limit | integer | Optional |  | Maximum limit of completed orders by counterparty  
user_country_limit | integer | Optional |  | KYC nationality restriction  
completed_rate_limit | number | Optional |  | 30-day completion rate limit  
user_orders_limit | integer | Optional |  | Maximum order limit for counterparty  
hide_payment | string | Optional |  | Whether payment methods are hidden. `1`: hidden; `0`: visible.  
currencyType | string | Optional |  | Cryptocurrency symbol.  
want_type | string | Optional |  | Fiat currency  
trade_tips | string | Optional |  | Trading terms  
new_hand | integer | Optional |  | Special ad type. `0` normal; `1` newcomer guide; `2` newcomer discount; `3` featured promo; `4` KOL ad; `5` coupon ad.  
id | string | Optional |  | Advertisement ID.  
status | string | Optional |  | Ad status: `OPEN` listed; `OFFLIN` delisted; `CLOSED` closed; `CANCEL` canceled.  
locked_amount | string | Optional |  | Ad frozen amount  
hide_rate | string | Optional |  | Hidden price  
is_out_time | integer | Optional |  | Whether the ad timed out. `1`: timed out; `0`: not yet.  
rate_ref_id | integer | Optional |  | Floating reference: `1` platform; `2` Gate; `3` spot; `<= 0` means fixed price.  
rate_offset | string | Optional |  | Floating ratio  
rate_fixed | integer | Optional |  | Price type: `0` floating; `1` fixed.  
float_trend | integer | Optional |  | Floating direction: `0` markup; `1` markdown.  
in_dispute | integer | Optional |  | Whether the ad had a disputed trade. `1`: yes; `0`: no.  
auto_reply | string | Optional |  | Auto reply data  
timestamp | integer | Optional |  | Ad creation time  
is_hedge | integer | Optional |  | Whether auto-delegation is enabled. `1`: yes; `0`: no.  
      
    
    {
      "timestamp": 0,
      "method": "string",
      "code": 0,
      "message": "string",
      "data": {
        "lists": [
          {}
        ]
      },
      "version": "string"
    }
    
    

##  UploadChatFile

Upload chat file request

Type | Constraints  
---|---  
object | required: ["image_content_type","base64_img"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
image_content_type | string | Required | enum: ["image/jpeg","image/jpg","image/png","video/mp4"] | File MIME type: supports `image/jpeg`, `image/jpg`, `image/png`, `video/mp4`.  
base64_img | string | Required |  | Base64-encoded file content.  
      
    
    {
      "image_content_type": "image/png",
      "base64_img": "iVBORw0KGgoAAAANSUhEUgAAAAEAAAAB..."
    }
    
    

##  P2pPreUploadChatFileResponse

P2pPreUploadChatFileResponse

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | number | Optional |  |   
method | string | Optional |  |   
code | integer | Optional |  |   
message | string | Optional |  |   
data | P2pPreUploadChatFileResult | Optional |  |   
version | string | Optional |  |   
  
**data**

P2pPreUploadChatFileResult

Type | Constraints  
---|---  
P2pPreUploadChatFileResult |   
      
    
    {
      "timestamp": 0,
      "method": "string",
      "code": 0,
      "message": "string",
      "data": {
        "url": "string",
        "fields": {
          "property1": "string",
          "property2": "string"
        },
        "file_key": "string"
      },
      "version": "string"
    }
    
    

##  PlaceBizPushOrder

Place ad order request

Type | Constraints  
---|---  
object | required: ["currencyType","exchangeType","type","unitPrice","number","payType"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
currencyType | string | Required |  | Cryptocurrency symbol.  
exchangeType | string | Required |  | Fiat currency  
type | string | Required | enum: ["0","1","2","3"] | Ad operation type. `0`: publish sell ad; `1`: publish buy ad; `2`: edit sell ad; `3`: edit buy ad.  
unitPrice | string | Required |  | Per-unit price in fixed-price mode.  
number | string | Required |  | Ad amount priced in `currencyType`.  
payType | string | Required |  | Payment types enabled for the ad, comma-separated; values can be obtained from `pay_type` in the payment method list, e.g. `bank`, `alipay`, `wechat`, `paypal`, `swift`, `wu`. `pay_type_json` uses the types in this field as keys to specify the corresponding payment accounts.  
pay_type_json | string | Optional |  | JSON string of specific payment accounts corresponding to `payType`. Each key is a payment type listed in `payType`, and each value is the current user's payment method ID for that type. For example, when `payType` is `bank,swift`, this field can be {"bank":"10001","swift":"10002"}.  
rateFixed | string | Optional |  | Price type: `0` floating; `1` fixed.  
oid | string | Optional |  | Pass ad ID when editing; omit or empty when publishing a new ad.  
minAmount | string | Optional |  | Minimum quantity per order, denominated by currencyType; required when limitBasis is not passed or is 0  
maxAmount | string | Optional |  | Maximum quantity per order, denominated by currencyType; required when limitBasis is not passed or is 0  
limitBasis | integer | Optional | enum: [0,1] | Trading limit unit. 0: by crypto quantity, 1: by fiat amount; defaults to 0 when not passed for a new ad. The limit unit of an existing ad cannot be changed when editing; a fiat-limit ad must keep passing 1 when edited  
fiatMinAmount | string | Optional |  | Minimum amount per order, denominated by exchangeType; required when limitBasis is 1  
fiatMaxAmount | string | Optional |  | Maximum amount per order, denominated by exchangeType; required when limitBasis is 1, and must not exceed the total fiat value of the ad quantity converted at the price  
tierLimit | string | Optional |  | Minimum counterparty VIP level; `0` means no requirement.  
verifiedLimit | string | Optional |  | Minimum counterparty verification level; `0` means no limit.  
regTimeLimit | string | Optional |  | Minimum counterparty account age in days; `0` means no limit.  
advertisersLimit | string | Optional |  | Whether trading with the advertiser is restricted. `0`: no; `1`: yes.  
polymarket_limit | integer | Optional | enum: [0,1] | Whether to restrict trading with Polymarket users. 0: no restriction, 1: restricted  
expire_min | string | Optional |  | Payment timeout in minutes.  
trade_tips | string | Optional |  | Advertisement trade terms displayed to ordering users; goes through off-platform traffic diversion risk control on submission, and when hit, the advertisement is not saved and code 70305102 is returned  
auto_reply | string | Optional |  | Auto reply content after order creation; goes through off-platform traffic diversion risk control on submission, and when hit, the advertisement is not saved and code 70305102 is returned  
min_completed_limit | string | Optional |  | Minimum completed orders for counterparty; `-1` unlimited.  
max_completed_limit | string | Optional |  | Maximum completed orders for counterparty; `-1` unlimited.  
completed_rate_limit | string | Optional |  | Counterparty minimum 30-day completion rate; `-1` means no limit.  
user_country_limit | string | Optional |  | KYC nationality restriction; `-1` means no restriction.  
user_order_limit | string | Optional |  | Maximum concurrent orders allowed for the counterparty. `-1`: unlimited.  
rateReferenceId | string | Optional |  | Floating price reference. `1`: platform reference; `2`: Gate reference; `3`: spot reference.  
rateOffset | string | Optional |  | Absolute floating offset ratio, e.g. `0.5` means 0.5%.  
float_trend | string | Optional |  | Floating direction: `0` markup; `1` markdown.  
team_payment_uid | string | Optional |  | Team payee UID; optional for non-team merchants.  
      
    
    {
      "currencyType": "USDT",
      "exchangeType": "USD",
      "type": "0",
      "unitPrice": "1.1",
      "number": "100",
      "payType": "bank,swift",
      "pay_type_json": "{\"bank\":\"10001\",\"swift\":\"10002\"}",
      "rateFixed": "1",
      "oid": "2124000001",
      "minAmount": "10",
      "maxAmount": "500",
      "limitBasis": 1,
      "fiatMinAmount": "100",
      "fiatMaxAmount": "1000",
      "tierLimit": "0",
      "verifiedLimit": "0",
      "regTimeLimit": "0",
      "advertisersLimit": "0",
      "polymarket_limit": 0,
      "expire_min": "20",
      "trade_tips": "Please pay from an account under your own name",
      "auto_reply": "Please tap Paid after completing the transfer",
      "min_completed_limit": "-1",
      "max_completed_limit": "-1",
      "completed_rate_limit": "-1",
      "user_country_limit": "-1",
      "user_order_limit": "-1",
      "rateReferenceId": "3",
      "rateOffset": "0.5",
      "float_trend": "0",
      "team_payment_uid": "1000001"
    }
    
    

##  P2pTransactionActionResponse

P2pTransactionActionResponse

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | number | Optional |  | Response timestamp.  
method | string | Optional |  | Placeholder for request method.  
code | integer | Optional |  | Response code, 0 means success  
message | string | Optional |  | Response message  
data | object | Optional |  | Empty object on success.  
version | string | Optional |  | API version.  
      
    
    {
      "timestamp": 0,
      "method": "string",
      "code": 0,
      "message": "string",
      "data": {},
      "version": "string"
    }
    
    

##  GetPendingTransactionListRequest

Get pending transaction list request

Type | Constraints  
---|---  
object | required: ["crypto_currency","fiat_currency"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
crypto_currency | string | Required |  | Cryptocurrency symbol.  
fiat_currency | string | Required |  | Fiat currency  
order_tab | string | Optional | enum: ["pending","dispute"] | Order tab: `pending` in progress (`OPEN`, `PAID`, `LOCKED`, `TEMP`); `dispute` in dispute; default `pending`.  
select_type | string | Optional |  | Order side filter: `buy` buy orders; `sell` sell orders; empty: all.  
status | string | Optional |  | Order status filter. `open` unpaid (`OPEN`); `paid` paid (`PAID`); `locked` locked (`LOCKED`);  
`dispute` in dispute; empty or omitted uses the default range for `order_tab`.  
txid | integer | Optional |  | Order ID  
start_time | integer | Optional |  | Start timestamp, default is 00:00 89 days ago  
end_time | integer | Optional |  | End timestamp, default is 23:59:59 today  
      
    
    {
      "crypto_currency": "USDT",
      "fiat_currency": "USD",
      "order_tab": "pending",
      "select_type": "sell",
      "status": "open",
      "txid": 40000001,
      "start_time": 1764547200,
      "end_time": 1767139199
    }
    
    

##  P2pMerchantBooksPlaceBizPushOrderResponse

P2pMerchantBooksPlaceBizPushOrderResponse

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | number | Optional |  | Response timestamp.  
method | string | Optional |  | Placeholder for request method.  
code | integer | Optional |  | Response code. 0 means success; 70305102 means the advertisement trade terms or auto reply hit off-platform traffic diversion risk control  
message | string | Optional |  | Response message  
data | object | Optional |  | Empty object when the advertisement is published or edited successfully; returns risk details when the advertisement content hits risk control  
version | string | Optional |  | API version.  
  
**data**

Empty object when the advertisement is published or edited successfully; returns risk details when the advertisement content hits risk control

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
risk_code | integer | Optional |  | Risk control sub-code; 0 for advertisement content traffic diversion risk control  
risk_event | object | Optional |  | Risk control prompt event for advertisement content  
  
**data / risk_event**

Risk control prompt event for advertisement content

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
type | string | Optional | enum: ["modal"] | Prompt display type  
title | string | Optional |  | Risk control prompt title  
msg | string | Optional |  | Risk control prompt message generated based on the field that hit risk control  
action | array | Optional |  | Available actions; advertisement content risk control only returns the close action  
content_risk_type | string | Optional | enum: ["trade_tips","auto_reply","trade_tips_auto_reply"] | Advertisement content field that hit risk control  
trade_tips | string | Optional |  | Prompt message returned when the trade terms hit risk control  
auto_reply | string | Optional |  | Prompt message returned when the auto reply hits risk control  
  
**data / risk_event / action**

Available actions; advertisement content risk control only returns the close action

Type | Constraints  
---|---  
array |   
  
**data / risk_event / action / items**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
action_type | string | Optional | enum: ["close"] | Action type  
title | string | Optional |  | Action button text  
mainly | integer | Optional | enum: [0] | Whether it is the primary action. 0: no  
action_data | object | Optional |  | Additional data of the action; empty object for the close action  
      
    
    {
      "timestamp": 0,
      "method": "string",
      "code": 0,
      "message": "string",
      "data": {
        "risk_code": 0,
        "risk_event": {
          "type": "modal",
          "title": "string",
          "msg": "string",
          "action": [],
          "content_risk_type": "trade_tips",
          "trade_tips": "string",
          "auto_reply": "string"
        }
      },
      "version": "string"
    }
    
    

##  P2pTransactionListResponse

P2pTransactionListResponse

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | number | Optional |  |   
method | string | Optional |  |   
code | integer | Optional |  |   
message | string | Optional |  |   
data | object | Optional |  |   
version | string | Optional |  |   
  
**data**

P2pTransactionListResult

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
list | array | Optional |  |   
trans_time | array | Optional |  | Countdown time  
count | integer | Optional |  | Number of orders  
exported_num | integer | Optional |  | Export count  
  
**data / list**

Type | Constraints  
---|---  
array |   
  
**data / list / items**

P2pTransactionListItem

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
type_buy | integer | Optional |  | Order side from current user's view. `1`: buy; `0`: sell.  
timest | string | Optional |  | Creation time of order  
timest_expire | string | Optional |  | Order expiration time  
timestamp | integer | Optional |  | Order creation timestamp  
rate | string | Optional |  | Order price in fiat currency.  
amount | string | Optional |  | Order size in cryptocurrency.  
total | string | Optional |  | Total fiat amount of the order.  
txid | integer | Optional |  | Order ID  
status | string | Optional |  | Display status: `unpay` awaiting payment; `paid` buyer paid; `unconfirmed` awaiting seller confirmation; `locked` locked; `finished` completed; `cancel` canceled; `expired` expired; `bclosed` arbitration filled; `sclosed` arbitration canceled.  
its_realname | string | Optional |  | Counterparty real name or verified display name.  
its_uid | string | Optional |  | Counterparty crypto UID.  
its_nick | string | Optional |  | Counterparty nickname  
seller_realname | string | Optional |  | Seller real name or verified display name.  
buyer_realname | string | Optional |  | Buyer real name or verified display name.  
cancelable | integer | Optional |  | Whether the order can be canceled. `1`: yes; `0`: no.  
currency_type | string | Optional |  | Cryptocurrency symbol.  
want_type | string | Optional |  | Fiat currency  
hide_payment | integer | Optional |  | Whether payment methods are hidden. `1`: hidden; `0`: visible.  
sel_paytype | string | Optional |  | Selected payment type for this order, e.g. `bank`, `alipay`, `wechat`, `paypal`, `swift`, `wu`.  
pay_others | array | Optional |  | Other payment method details; may appear on historical orders.  
cd_time | integer | Optional |  | Countdown seconds for the current order.  
order_type | integer | Optional |  | Order type: `1` standard; `2` partner; `3` flash swap; `4` Web3.  
order_tag | array | Optional |  | Order tags  
convert_info | object | Optional |  | Flash swap order information  
  
**data / list / items / pay_others**

Other payment method details; may appear on historical orders.

Type | Constraints  
---|---  
array |   
  
**data / list / items / pay_others / items**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
pay_type | string | Optional |  | Payment method type  
pay_name | string | Optional |  | Payment method name  
  
**data / list / items / order_tag**

Order tags

Type | Constraints  
---|---  
array |   
  
**data / list / items / order_tag / items**

Type | Constraints  
---|---  
string |   
  
**data / list / items / convert_info**

P2pTransactionConvertInfo

Flash swap order information

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
convert_type | string | Optional |  | Flash swap target currency  
convert_status | string | Optional |  | Flash swap order status  
pre_rate | string | Optional |  | Expected price when placing order  
rate | string | Optional |  | Execution price  
pre_fiat_rate | string | Optional |  | Expected fiat price when placing order  
fiat_rate | string | Optional |  | Fiat price at execution  
amount | string | Optional |  | Size  
convert_amount | string | Optional |  | Swap Amount  
slippage | string | Optional |  | Slippage calculation: slippage = (expected price when placing order - real-time price during auto swap) / expected price when placing order  
status | string | Optional |  | Flash swap order display status  
  
**data / trans_time**

Countdown time

Type | Constraints  
---|---  
array |   
  
**data / trans_time / items**

P2pTransactionTimeMarker

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
od_time | integer | Optional |  |   
      
    
    {
      "timestamp": 0,
      "method": "string",
      "code": 0,
      "message": "string",
      "data": {
        "list": [
          {}
        ],
        "trans_time": [
          {}
        ],
        "count": 0,
        "exported_num": 0
      },
      "version": "string"
    }
    
    

##  ConfirmPayment

Confirm payment request

Type | Constraints  
---|---  
object | required: ["txid"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
txid | string | Required |  | Order ID  
payment_method | string | Optional |  | Payment type used for this payment; optional but must be among order-supported types. Use `supported_pay_types` on the order or `pay_type` list, e.g. `bank`, `alipay`, `wechat`, `paypal`, `swift`, `wu`.  
      
    
    {
      "txid": "40000001",
      "payment_method": "bank"
    }
    
    

##  AdsDetailRequest

Get ad details request

Type | Constraints  
---|---  
object | required: ["adv_no"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
adv_no | string | Required |  | Advertisement ID.  
      
    
    {
      "adv_no": "2124000001"
    }
    
    

##  P2pAdsListResponse

P2pAdsListResponse

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | number | Optional |  |   
method | string | Optional |  |   
code | integer | Optional |  |   
message | string | Optional |  |   
data | array | Optional |  |   
version | string | Optional |  |   
  
**data**

Type | Constraints  
---|---  
array |   
  
**data / items**

P2pAdsListItem

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
index | integer | Optional |  | Serial number  
asset | string | Optional |  | Cryptocurrency  
fiat_unit | string | Optional |  | Fiat currency  
adv_no | integer | Optional |  | Ad ID  
price | string | Optional |  | Price  
surplus_amount | string | Optional |  | Remaining tradable crypto quantity  
max_single_trans_amount | string | Optional |  | Maximum crypto size per trade.  
min_single_trans_amount | string | Optional |  | Minimum crypto size per trade.  
fiat_min_amount | string | Optional |  | Minimum fiat amount per order  
fiat_max_amount | string | Optional |  | Maximum fiat amount per order  
limit_basis | integer | Optional | enum: [0,1] | Trading limit unit. 0: crypto quantity, 1: fiat amount  
limit_basis_text | string | Optional | enum: ["crypto","fiat"] | Trading limit unit label. crypto: crypto quantity, fiat: fiat amount  
trade_methods | array | Optional |  | Supported payment methods list  
nick_name | string | Optional |  | Advertiser Nickname  
  
**data / items / trade_methods**

Supported payment methods list

Type | Constraints  
---|---  
array |   
  
**data / items / trade_methods / items**

P2pAdsListTradeMethod

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
icon_url_color | string | Optional |  | Payment method color icon URL  
identifier | string | Optional |  | Payment method identifier  
pay_id | string | Optional |  | Payment method ID  
pay_type | string | Optional |  | Payment method type  
trade_method_name | string | Optional |  | Payment method name  
      
    
    {
      "timestamp": 0,
      "method": "string",
      "code": 0,
      "message": "string",
      "data": [
        {
          "index": 0,
          "asset": "string",
          "fiat_unit": "string",
          "adv_no": 0,
          "price": "string",
          "surplus_amount": "string",
          "max_single_trans_amount": "string",
          "min_single_trans_amount": "string",
          "fiat_min_amount": "string",
          "fiat_max_amount": "string",
          "limit_basis": 0,
          "limit_basis_text": "crypto",
          "trade_methods": [],
          "nick_name": "string"
        }
      ],
      "version": "string"
    }
    
    

##  MyAdsListRequest

Get my ads list request

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
asset | string | Optional |  | Crypto asset; omit to skip asset filter.  
fiat_unit | string | Optional |  | Fiat currency; omit to skip fiat filter.  
trade_type | string | Optional |  | Ad side: `buy` for buy-crypto ads, `sell` for sell-crypto ads; omit for all sides.  
      
    
    {
      "asset": "USDT",
      "fiat_unit": "USD",
      "trade_type": "sell"
    }
    
    

##  P2pChatListResponse

P2pChatListResponse

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | number | Optional |  |   
method | string | Optional |  |   
code | integer | Optional |  |   
message | string | Optional |  |   
data | object | Optional |  |   
version | string | Optional |  |   
  
**data**

P2pChatListResult

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
messages | array | Optional |  | Message List  
memo | string | Optional |  | Payment tip (displayed on homepage only)  
has_history | boolean | Optional |  | Whether historical records exist  
txid | integer | Optional |  | Order ID  
SRVTM | integer | Optional |  | Timestamp of the latest message.  
order_status | string | Optional |  | Raw order status in DB; typical values: `OPEN`, `PAID`, `LOCKED`, `ACCEPT`, `BCLOSED`, `CANCEL`, `BECANCEL`, `SCLOSED`, `SCANCEL`.  
  
**data / messages**

Message List

Type | Constraints  
---|---  
array |   
  
**data / messages / items**

P2pChatMessage

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
is_sell | integer | Optional |  | Whether the current user is the seller. `1`: yes; `0`: no.  
msg_type | integer | Optional |  | Message type: `0` text; `1` file; `2` template; `3` order-share; `4` payment-share; `5` status update.  
msg | string | Optional |  | Message content; for file messages, usually URL or file key.  
username | string | Optional |  | Message sender username  
timest | integer | Optional |  | Message timestamp  
msg_obj | object | Optional |  |   
uid | string | Optional |  | Sender's crypto UID; system messages may use `System` or an empty string.  
type | integer | Optional |  | Display type: `1` file message; `2` system message.  
pic | string | Optional |  | File link  
file_key | string | Optional |  | File key  
file_type | string | Optional |  | File type: `image` for images, `video` for videos.  
risk_type | integer | Optional | enum: [1] | Risk control display type. 1: off-platform traffic diversion risk; returned when a text message hits risk control  
toast_msg | string | Optional |  | Risk control prompt message; returned only when risk_type=1  
  
**data / messages / items / msg_obj**

P2pChatMessagePayload

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
status | string | Optional |  | Order status when sending a message. Typical values: `OPEN`, `PAID`, `LOCKED`, `ACCEPT`, `BCLOSED`, `CANCEL`, `BECANCEL`, `SCLOSED`, `SCANCEL`.  
text | string | Optional |  | Message content  
payment_voucher | array | Optional |  | Payment voucher  
reason_id | integer | Optional |  | Cancel reason ID. `1` no longer want to buy; `2` cannot reach seller; `3` will not pay; `4` seller account not real; `5` payout account issue; `6` price mismatch; `7` mutually agreed cancel; `8` poor communication; `9` other; `10` seller cannot release with refund; `11` terms not met; `12` seller payout risk-controlled.  
toast_id | integer | Optional |  | Cancellation reason popup  
reason_memo | string | Optional |  | Cancel reason description.  
cancel_time | integer | Optional |  | Cancellation time  
seller_confirm | integer | Optional |  | Seller confirmation of cancel reason: `0` pending; `1` confirmed; `2` rejected.  
id | string | Optional |  | Payment method information ID  
account_des | string | Optional |  | Payment method description  
pay_type | string | Optional |  | Payment method type  
file | string | Optional |  | Payment method file link  
file_key | string | Optional |  | Payment method file key  
account | string | Optional |  | Payment account or masked payment account.  
memo | string | Optional |  | Payment method note  
code | string | Optional |  | Payment method code  
memo_ext | string | Optional |  | Payment method additional note  
trade_tips | string | Optional |  | Payment method tip  
real_name | string | Optional |  | Payment method username  
is_delete | integer | Optional |  | Whether the payment method was deleted. `1`: deleted; `0`: not deleted.  
pay_name | string | Optional |  | Payment method full name  
  
**data / messages / items / msg_obj / payment_voucher**

Payment voucher

Type | Constraints  
---|---  
array |   
  
**data / messages / items / msg_obj / payment_voucher / items**

Type | Constraints  
---|---  
string |   
      
    
    {
      "timestamp": 0,
      "method": "string",
      "code": 0,
      "message": "string",
      "data": {
        "messages": [
          {}
        ],
        "memo": "string",
        "has_history": true,
        "txid": 0,
        "SRVTM": 0,
        "order_status": "string"
      },
      "version": "string"
    }
    
    

##  P2pAdDetailResponse

P2pAdDetailResponse

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | number | Optional |  |   
method | string | Optional |  |   
code | integer | Optional |  |   
message | string | Optional |  |   
data | object | Optional |  |   
version | string | Optional |  |   
  
**data**

P2pAdDetail

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
rate | string | Optional |  | Advertisement price.  
type | string | Optional |  | Ad side: `buy` buy-crypto ad; `sell` sell-crypto ad.  
amount | string | Optional |  | Remaining crypto amount on the ad.  
min_amount | string | Optional |  | Minimum quantity per order, denominated by currency_type  
max_amount | string | Optional |  | Maximum quantity per order, denominated by currency_type  
fiat_min_amount | string | Optional |  | Minimum trade amount in `want_type`.  
fiat_max_amount | string | Optional |  | Maximum trade amount priced in `want_type`.  
limit_basis | integer | Optional | enum: [0,1] | Trading limit unit. 0: crypto quantity, 1: fiat amount  
limit_basis_text | string | Optional | enum: ["crypto","fiat"] | Trading limit unit label. crypto: crypto quantity, fiat: fiat amount  
total | string | Optional |  | Fiat amount  
pay_ali | integer | Optional |  | Whether Alipay is supported. `1`: yes; `0`: no.  
pay_bank | integer | Optional |  | Whether bank transfer is supported. `1`: yes; `0`: no.  
pay_paypal | integer | Optional |  | Whether PayPal is supported. `1`: yes; `0`: no.  
pay_wechat | integer | Optional |  | Whether WeChat Pay is supported. `1`: yes; `0`: no.  
pay_type_num | string | Optional |  | Payment method ID list  
pay_type_json | string | Optional |  | JSON map of payment type -> payment method ID.  
locked_amount | string | Optional |  | Locked amount  
orderid | integer | Optional |  | Order ID  
timestamp | integer | Optional |  | Created time  
currency_type | string | Optional |  | Cryptocurrency symbol.  
want_type | string | Optional |  | Fiat type  
hide_rate | string | Optional |  | Hidden price  
trade_tips | string | Optional |  | Trading terms  
auto_reply | string | Optional |  | Auto reply  
rate_ref_id | integer | Optional |  | Floating reference: `1` platform; `2` Gate; `3` spot; `<= 0` means fixed price.  
rate_offset | number | Optional |  | Floating ratio (absolute value)  
status | string | Optional |  | Ad status: `OPEN` listed; `OFFLIN` delisted; `CLOSED` closed; `CANCEL` canceled.  
rate_fixed | integer | Optional |  | Price type: `0` floating; `1` fixed.  
float_trend | integer | Optional |  | Floating direction: `0` markup; `1` markdown.  
expire_min | integer | Optional |  | Timeout (minutes)  
tier_limit | integer | Optional |  | Tier limit  
reg_time_limit | integer | Optional |  | Registration time limit  
advertisers_limit | integer | Optional |  | Whether trading with the advertiser is restricted. `0`: no; `1`: yes.  
polymarket_limit | integer | Optional |  | Whether to restrict trading with Polymarket users. 0: no restriction, 1: restricted  
min_completed_limit | integer | Optional |  | Minimum limit of completed orders  
max_completed_limit | integer | Optional |  | Maximum limit of completed orders  
user_orders_limit | integer | Optional |  | Order count limit  
completed_rate_limit | number | Optional |  | 30-day completion rate limit  
limit_country_cn | string | Optional |  | Restricted nationality (Chinese)  
limit_country_en | string | Optional |  | Restricted nationality (English)  
is_hedge | integer | Optional |  | Whether auto-delegation is enabled. `1`: yes; `0`: no.  
hide_payment | integer | Optional |  | Whether payment methods are hidden. `1`: hidden; `0`: visible.  
      
    
    {
      "timestamp": 0,
      "method": "string",
      "code": 0,
      "message": "string",
      "data": {
        "rate": "string",
        "type": "string",
        "amount": "string",
        "min_amount": "string",
        "max_amount": "string",
        "fiat_min_amount": "string",
        "fiat_max_amount": "string",
        "limit_basis": 0,
        "limit_basis_text": "crypto",
        "total": "string",
        "pay_ali": 0,
        "pay_bank": 0,
        "pay_paypal": 0,
        "pay_wechat": 0,
        "pay_type_num": "string",
        "pay_type_json": "string",
        "locked_amount": "string",
        "orderid": 0,
        "timestamp": 0,
        "currency_type": "string",
        "want_type": "string",
        "hide_rate": "string",
        "trade_tips": "string",
        "auto_reply": "string",
        "rate_ref_id": 0,
        "rate_offset": 0,
        "status": "string",
        "rate_fixed": 0,
        "float_trend": 0,
        "expire_min": 0,
        "tier_limit": 0,
        "reg_time_limit": 0,
        "advertisers_limit": 0,
        "polymarket_limit": 0,
        "min_completed_limit": 0,
        "max_completed_limit": 0,
        "user_orders_limit": 0,
        "completed_rate_limit": 0,
        "limit_country_cn": "string",
        "limit_country_en": "string",
        "is_hedge": 0,
        "hide_payment": 0
      },
      "version": "string"
    }
    
    

##  P2pUploadChatFileResponse

P2pUploadChatFileResponse

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | number | Optional |  |   
method | string | Optional |  |   
code | integer | Optional |  |   
message | string | Optional |  |   
data | object | Optional |  |   
version | string | Optional |  |   
  
**data**

P2pUploadChatFileResult

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
file_key | string | Optional |  | File key  
      
    
    {
      "timestamp": 0,
      "method": "string",
      "code": 0,
      "message": "string",
      "data": {
        "file_key": "string"
      },
      "version": "string"
    }
    
    

##  AdsUpdateStatus

Ad status update request

Type | Constraints  
---|---  
object | required: ["adv_no","adv_status"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
adv_no | integer | Required |  | Advertisement ID.  
adv_status | integer | Required | enum: [1,3,4] | Ad status. `1`: listed; `3`: delisted; `4`: closed.  
      
    
    {
      "adv_no": 2124000001,
      "adv_status": 3
    }
    
    

##  ConfirmReceipt

Confirm receipt request

Type | Constraints  
---|---  
object | required: ["txid"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
txid | string | Required |  | Order ID  
      
    
    {
      "txid": "40000001"
    }
    
    

##  P2pPaymentMethodsResponse

P2pPaymentMethodsResponse

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | number | Optional |  |   
method | string | Optional |  |   
code | integer | Optional |  |   
message | string | Optional |  |   
data | array | Optional |  |   
version | string | Optional |  |   
  
**data**

Type | Constraints  
---|---  
array |   
  
**data / items**

P2pPaymentMethodGroup

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
pay_type | string | Optional |  | Payment method type  
pay_name | string | Optional |  | Payment method name  
ids | array | Optional |  | User's currently bound payment method (primary key ID)  
list | array | Optional |  |   
  
**data / items / ids**

User's currently bound payment method (primary key ID)

Type | Constraints  
---|---  
array |   
  
**data / items / ids / items**

Type | Constraints  
---|---  
integer |   
  
**data / items / list**

Type | Constraints  
---|---  
array |   
  
**data / items / list / items**

P2pPaymentMethodAccount

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
uid | integer | Optional |  | useruID  
bankid | string | Optional |  | User's currently bound payment method (primary key ID)  
nickname | integer | Optional |  | Cardholder UID  
bankname | string | Optional |  | Bank name  
bankbranch | string | Optional |  | Bank branch name  
bankcity | string | Optional |  | Bank city  
bankprov | string | Optional |  | Bank province  
bankaddr | string | Optional |  | Bank card number or masked card number.  
bankdesc | string | Optional |  | Bank note  
hold_uid | integer | Optional |  | Cardholder UID  
hold_username | string | Optional |  | Cardholder name  
real_name | string | Optional |  | User verified display name.  
id | string | Optional |  | User's currently bound payment method (primary key ID)  
account_des | string | Optional |  | Payment method description  
pay_type | string | Optional |  | Payment method type  
file | string | Optional |  | Payment method file link  
file_key | string | Optional |  | Payment method file key  
account | string | Optional |  | Payment account or masked payment account.  
memo | string | Optional |  | Payment method note  
code | string | Optional |  | Payment method code  
memo_ext | string | Optional |  | Payment method additional note  
trade_tips | string | Optional |  | Payment method transaction information  
      
    
    {
      "timestamp": 0,
      "method": "string",
      "code": 0,
      "message": "string",
      "data": [
        {
          "pay_type": "string",
          "pay_name": "string",
          "ids": [],
          "list": []
        }
      ],
      "version": "string"
    }
    
    

##  CancelOrder

Cancel order request

Type | Constraints  
---|---  
object | required: ["txid"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
txid | string | Required |  | Order ID  
reason_id | string | Optional |  | Cancel reason ID. `1` no longer want to buy; `2` cannot reach seller; `3` will not pay; `4` seller account not real; `5` payout account issue; `6` price mismatch; `7` mutually agreed cancel; `8` poor communication; `9` other; `10` seller cannot release with refund; `11` terms not met; `12` seller payout risk-controlled.  
reason_memo | string | Optional |  | Extra cancel notes when `reason_id` is `9` or explanation is required.  
      
    
    {
      "txid": "40000001",
      "reason_id": "1",
      "reason_memo": "Canceled after agreement with the counterparty"
    }
    
    

##  P2pAdsUpdateStatusResponse

P2pAdsUpdateStatusResponse

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | number | Optional |  |   
method | string | Optional |  |   
code | integer | Optional |  |   
message | string | Optional |  |   
data | object | Optional |  |   
version | string | Optional |  |   
  
**data**

P2pAdsUpdateStatusResult

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
status | integer | Optional |  | Ad status after update: `1` listed; `3` delisted; `4` closed.  
      
    
    {
      "timestamp": 0,
      "method": "string",
      "code": 0,
      "message": "string",
      "data": {
        "status": 0
      },
      "version": "string"
    }
    
    

##  GetCounterpartyUserInfoRequest

Get counterparty user info request

Type | Constraints  
---|---  
object | required: ["biz_uid"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
biz_uid | string | Required |  | Counterparty crypto UID from order list or detail field `its_uid`.  
      
    
    {
      "biz_uid": "biz_uid_demo_9f3a7c"
    }
    
    

##  P2pTransactionDetailResponse

P2pTransactionDetailResponse

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | number | Optional |  |   
method | string | Optional |  |   
code | integer | Optional |  |   
message | string | Optional |  |   
data | object | Optional |  |   
version | string | Optional |  |   
  
**data**

P2pTransactionDetail

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
is_sell | integer | Optional |  | Whether the current user is the seller. `1`: yes; `0`: no.  
txid | integer | Optional |  | Order ID (txid).  
orderid | integer | Optional |  | ID of the posted order (orderid).  
timest | integer | Optional |  | Order creation timestamp  
last_pay_time | integer | Optional |  | Payment deadline  
remain_pay_time | integer | Optional |  | Seconds left to pay; `<= 0` means overdue.  
currency_type | string | Optional |  | Cryptocurrency symbol.  
want_type | string | Optional |  | Fiat currency  
symbol | string | Optional |  | Fiat currency symbol  
rate | string | Optional |  | Order price in `want_type` units.  
amount | string | Optional |  | Order size in cryptocurrency.  
total | string | Optional |  | Total fiat amount of the order.  
status | string | Optional |  | Display status: `unpay` unpaid; `hide_payment` unpaid with payment info hidden; `paid` buyer paid; `unconfirmed` awaiting seller confirmation; `locked` locked; `finished` done; `cancel` canceled; `expired` expired; `bclosed` arbitration filled; `sclosed` arbitration canceled.  
reason_id | string | Optional |  | Cancel reason ID; empty string means none. Examples: `1` no longer want to buy; `2` cannot reach seller; `3` will not pay; `4` seller did not provide a real account; `6` price/amount mismatch; `9` other; `10` seller cannot release and refund issued; `11` terms not met; `12` seller payout account risk-controlled.  
reason_desc | string | Optional |  | Cancel reason description.  
cancel_time | string | Optional |  | Cancellation time  
in_appeal | integer | Optional |  | Whether a dispute is active. `1`: yes; `0`: no.  
dispute_time | integer | Optional |  | Earliest timestamp when a dispute may be opened.  
cancelable | integer | Optional |  | Whether cancellation is allowed. `1`: yes; `0`: no.  
hide_payment | integer | Optional |  | Whether payment methods are hidden. `1`: hidden; `0`: visible.  
trade_tips | string | Optional |  | Trading terms  
show_bank | string | Optional |  | Whether to show bank transfer details. `1`: show; `0`: hide.  
bankname | string | Optional |  | Bank name  
bankbranch | string | Optional |  | Bank branch name  
bankid | string | Optional |  | Bank account or masked account.  
bank_holder_realname | string | Optional |  | Bank cardholder name  
show_ali | string | Optional |  | Whether to show Alipay details. `1`: show; `0`: hide.  
aliname | string | Optional |  | Alipay account name  
is_alicode | integer | Optional |  | Whether an Alipay QR exists. `1`: yes; `0`: no.  
show_wechat | string | Optional |  | Whether to show WeChat details. `1`: show; `0`: hide.  
wename | string | Optional |  | WeChat account name  
show_others | string | Optional |  | Whether to show other payment methods. `1`: show; `0`: hide.  
pay_others | array | Optional |  | Other payment methods  
sel_paytype | string | Optional |  | Selected payment type for this order, e.g. `bank`, `alipay`, `wechat`, `paypal`, `swift`, `wu`.  
its_uid | string | Optional |  | Counterparty crypto UID.  
its_nickname | string | Optional |  | Counterparty nickname  
its_realname | string | Optional |  | Counterparty real name or verified display name.  
have_traded | integer | Optional |  | Whether you traded with the counterparty before. `1`: yes; `0`: no.  
appeal_allow_cancel | integer | Optional |  | Whether the dispute can be withdrawn. `1`: allowed; `0`: not allowed.  
appeal_verdict_has_open | string | Optional |  | Dispute outcome or in-dispute notice text.  
im_unread | integer | Optional |  | Unread chat message count.  
payment_voucher_url | array | Optional |  | Payment voucher  
timest_paid | integer | Optional |  | Timestamp when the buyer confirmed payment.  
own_realname | string | Optional |  | Current user's real name or verified display name.  
order_type | integer | Optional |  | Order type: `1` standard; `2` partner; `3` flash swap; `4` Web3.  
is_show_receive | integer | Optional |  | Whether to show confirm-receipt during dispute. `1`: show; `0`: hide.  
show_seller_contact_info | boolean | Optional |  | Whether to display seller contact information  
supported_pay_types | array | Optional |  | Supported payment method types for the order, e.g. `bank`, `alipay`, `wechat`, `paypal`, `swift`, `wu`.  
  
**data / pay_others**

Other payment methods

Type | Constraints  
---|---  
array |   
  
**data / pay_others / items**

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
id | string | Optional |  | Payment method record ID.  
account_des | string | Optional |  | Payment method description  
pay_type | string | Optional |  | Payment method type  
account | string | Optional |  | Payment account or masked account.  
memo | string | Optional |  | Payment note or memo.  
trade_tips | string | Optional |  | Payment instructions or tips.  
pay_name | string | Optional |  | Display name of the payment method.  
  
**data / payment_voucher_url**

Payment voucher

Type | Constraints  
---|---  
array |   
  
**data / payment_voucher_url / items**

Type | Constraints  
---|---  
string |   
  
**data / supported_pay_types**

Supported payment method types for the order, e.g. `bank`, `alipay`, `wechat`, `paypal`, `swift`, `wu`.

Type | Constraints  
---|---  
array |   
  
**data / supported_pay_types / items**

Type | Constraints  
---|---  
string |   
      
    
    {
      "timestamp": 0,
      "method": "string",
      "code": 0,
      "message": "string",
      "data": {
        "is_sell": 0,
        "txid": 0,
        "orderid": 0,
        "timest": 0,
        "last_pay_time": 0,
        "remain_pay_time": 0,
        "currency_type": "string",
        "want_type": "string",
        "symbol": "string",
        "rate": "string",
        "amount": "string",
        "total": "string",
        "status": "string",
        "reason_id": "string",
        "reason_desc": "string",
        "cancel_time": "string",
        "in_appeal": 0,
        "dispute_time": 0,
        "cancelable": 0,
        "hide_payment": 0,
        "trade_tips": "string",
        "show_bank": "string",
        "bankname": "string",
        "bankbranch": "string",
        "bankid": "string",
        "bank_holder_realname": "string",
        "show_ali": "string",
        "aliname": "string",
        "is_alicode": 0,
        "show_wechat": "string",
        "wename": "string",
        "show_others": "string",
        "pay_others": [
          {}
        ],
        "sel_paytype": "string",
        "its_uid": "string",
        "its_nickname": "string",
        "its_realname": "string",
        "have_traded": 0,
        "appeal_allow_cancel": 0,
        "appeal_verdict_has_open": "string",
        "im_unread": 0,
        "payment_voucher_url": [
          "string"
        ],
        "timest_paid": 0,
        "own_realname": "string",
        "order_type": 0,
        "is_show_receive": 0,
        "show_seller_contact_info": true,
        "supported_pay_types": [
          "string"
        ]
      },
      "version": "string"
    }
    
    

##  AdsListRequest

Get market ads list request

Type | Constraints  
---|---  
object | required: ["asset","fiat_unit","trade_type"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
asset | string | Required |  | Cryptocurrency symbol.  
fiat_unit | string | Required |  | Fiat currency  
trade_type | string | Required |  | Ad side: `buy` buy-crypto ad; `sell` sell-crypto ad.  
      
    
    {
      "asset": "USDT",
      "fiat_unit": "USD",
      "trade_type": "sell"
    }
    
    

##  GetMyselfPaymentRequest

Get payment method list request

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
fiat | string | Optional |  | Fiat currency; omit to return all available payment methods.  
      
    
    {
      "fiat": "USD"
    }
    
    

##  P2pMerchantUserInfoResponse

P2pMerchantUserInfoResponse

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
timestamp | number | Optional |  |   
method | string | Optional |  |   
code | integer | Optional |  |   
message | string | Optional |  |   
data | object | Optional |  |   
version | string | Optional |  |   
  
**data**

P2pMerchantUserInfo

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
is_self | boolean | Optional |  | Whether self  
user_timest | string | Optional |  | User registration time (formatted string)  
counterparties_num | integer | Optional |  | Number of counterparties  
email_verified | string | Optional |  | Whether email is verified. `1`: yes; `0`: no.  
verified | string | Optional |  | Whether KYC is completed. `1`: yes; `0`: no.  
has_phone | string | Optional |  | Whether a phone number is bound. `1`: yes; `0`: no.  
user_name | string | Optional |  | Username  
user_note | string | Optional |  | User note information  
complete_transactions | string | Optional |  | Total completed orders  
paid_transactions | string | Optional |  | Number of completed buy orders  
accepted_transactions | string | Optional |  | Number of completed sell orders  
transactions_used_time | string | Optional |  | Average time to confirm receipt  
cancelled_used_time_month | string | Optional |  | Cancellation time in last 30 days  
complete_transactions_month | string | Optional |  | Number of completed orders in last 30 days  
complete_rate_month | number | Optional |  | Completion rate in last 30 days  
orders_buy_rate_month | number | Optional |  | Buy order ratio in last 30 days  
is_black | integer | Optional |  | Whether the user is blocked. `1`: yes; `0`: no.  
is_follow | integer | Optional |  | Whether you follow this user. `1`: yes; `0`: no.  
have_traded | integer | Optional |  | Whether you have traded with this user before. `1`: yes; `0`: no.  
biz_uid | string | Optional |  | Encrypted UID  
blue_vip | integer | Optional |  | Blue V Crown Shield  
work_status | integer | Optional |  | Merchant work status  
registration_days | integer | Optional |  | Registration days  
first_trade_days | integer | Optional |  | Days since first trade  
need_replenish | integer | Optional |  | Whether additional margin is required. `1`: yes; `0`: no.  
merchant_info | object | Optional |  | Markets where user can place orders  
online_status | integer | Optional |  | Merchant online status: `1` online; `0` offline.  
work_hours | object|null | Optional | nullable: true | Merchant online status details  
transactions_month | number | Optional |  | 30-day transaction volume  
transactions_all | number | Optional |  | Total transaction volume  
trade_versatile | boolean | Optional |  | Single user or composite user  
  
**data / merchant_info**

P2pMerchantMarketInfo

Markets where user can place orders

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
type | string | Optional |  |   
market | string | Optional |  |   
      
    
    {
      "timestamp": 0,
      "method": "string",
      "code": 0,
      "message": "string",
      "data": {
        "is_self": true,
        "user_timest": "string",
        "counterparties_num": 0,
        "email_verified": "string",
        "verified": "string",
        "has_phone": "string",
        "user_name": "string",
        "user_note": "string",
        "complete_transactions": "string",
        "paid_transactions": "string",
        "accepted_transactions": "string",
        "transactions_used_time": "string",
        "cancelled_used_time_month": "string",
        "complete_transactions_month": "string",
        "complete_rate_month": 0,
        "orders_buy_rate_month": 0,
        "is_black": 0,
        "is_follow": 0,
        "have_traded": 0,
        "biz_uid": "string",
        "blue_vip": 0,
        "work_status": 0,
        "registration_days": 0,
        "first_trade_days": 0,
        "need_replenish": 0,
        "merchant_info": {
          "type": "string",
          "market": "string"
        },
        "online_status": 0,
        "work_hours": {},
        "transactions_month": 0,
        "transactions_all": 0,
        "trade_versatile": true
      },
      "version": "string"
    }
    
    

##  SetMerchantWorkHoursRequest

Request to set merchant working status or custom working hours

Type | Constraints  
---|---  
object | required: ["work_status"]  
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
work_status | integer | Required | enum: [0,1,2] | Working status. 0: resting, 1: working, 2: using custom working hours  
cycle_type | string | Optional | enum: ["Weekly","Daily"] | Custom working cycle; required when work_status is 2  
day_of_week | string | Optional |  | Weekly working days, comma-separated values 1-7 for Monday to Sunday; required when work_status is 2 and cycle_type is Weekly  
time_zone | string | Optional |  | UTC timezone offset, ranging from -12 to +14; required when work_status is 2  
start_time | string | Optional |  | Custom working start time in HH:mm format; required when work_status is 2 and must not be later than end_time  
end_time | string | Optional |  | Custom working end time in HH:mm format; required when work_status is 2 and must not be earlier than start_time  
      
    
    {
      "work_status": 2,
      "cycle_type": "Weekly",
      "day_of_week": "1,2,3,4,5",
      "time_zone": "+8",
      "start_time": "09:00",
      "end_time": "18:00"
    }
    
    

##  P2pPreUploadChatFileResult

P2pPreUploadChatFileResult

Type | Constraints  
---|---  
object |   
  
**Properties**

Name | Type | Required | Constraints | Description  
---|---|---|---|---  
url | string | Optional |  | S3 POST upload URL. Use it before the credentials expire.  
fields | object | Optional |  | Signed S3 form fields. Submit all keys and values unchanged when uploading.  
file_key | string | Optional |  | Chat file identifier. After uploading, use it as message in send_chat_message with type=1.  
  
**fields**

Signed S3 form fields. Submit all keys and values unchanged when uploading.

Type | Constraints  
---|---  
object |   
  
**fields / additionalProperties**

Type | Constraints  
---|---  
string |   
      
    
    {
      "url": "string",
      "fields": {
        "property1": "string",
        "property2": "string"
      },
      "file_key": "string"
    }